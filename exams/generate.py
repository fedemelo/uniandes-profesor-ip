"""Generate unique exam variants from a question bank.

Given a question bank where each question slot can have multiple variant files,
this script generates N unique exams (one per student) that maximize diversity
in both question selection and ordering.

Output is a single .tex file containing all exams back-to-back, producing a
single PDF for easy printing.
"""

import argparse
import collections
import itertools
import math
import os
import pathlib
import random
import shutil
import subprocess
import tomllib
from typing import NamedTuple


class QuestionSlot(NamedTuple):
    """A question directory with its available variant files."""

    name: str  # e.g., "q1"
    variants: list[str]  # paths relative to repo root, e.g., ["exams/questions/n1/q1/v1.tex"]


class ExamAssignment(NamedTuple):
    """A specific exam: which variant for each slot, in which order."""

    variant_indices: tuple[int, ...]  # which variant index per slot (in original q1..qN order)
    ordering: tuple[int, ...]  # permutation of slot indices defining question order


def load_config(path: str) -> dict:
    """Load and validate a TOML exam configuration file."""
    config_path = pathlib.Path(path)
    if not config_path.is_file():
        raise SystemExit(f"Error: Config file not found: {config_path}")

    with open(config_path, "rb") as f:
        config = tomllib.load(f)

    required = {
        "exam.name": str,
        "exam.title": str,
        "exam.semester": str,
        "exam.date": str,
        "exam.num_students": int,
        "exam.seed": int,
    }

    for dotted_key, expected_type in required.items():
        parts = dotted_key.split(".")
        val = config
        for part in parts:
            if not isinstance(val, dict) or part not in val:
                raise SystemExit(f"Error: Missing required config key: {dotted_key}")
            val = val[part]
        if not isinstance(val, expected_type):
            raise SystemExit(
                f"Error: Config key {dotted_key} must be {expected_type.__name__}, "
                f"got {type(val).__name__}"
            )

    if config["exam"]["num_students"] < 1:
        raise SystemExit("Error: num_students must be >= 1")

    return config


def scan_question_bank(
    questions_dir: pathlib.Path, exam_name: str
) -> tuple[list[QuestionSlot], str | None]:
    """Scan the question bank directory for an exam.

    Returns (slots, preamble_path) where preamble_path is None if no preamble.tex exists.
    """
    base = questions_dir / exam_name
    if not base.is_dir():
        raise SystemExit(f"Error: Question bank directory not found: {base}")

    repo_root = questions_dir.parent.parent

    preamble = base / "preamble.tex"
    preamble_path = str(preamble.relative_to(repo_root)) if preamble.is_file() else None

    slots = []
    for entry in sorted(base.iterdir()):
        if entry.is_dir() and entry.name.startswith("q"):
            variants = sorted(
                str(f.relative_to(repo_root))
                for f in entry.iterdir()
                if f.suffix == ".tex" and f.name.startswith("v")
            )
            if not variants:
                raise SystemExit(f"Error: No variant files (v*.tex) found in {entry}")
            slots.append(QuestionSlot(name=entry.name, variants=variants))

    if not slots:
        raise SystemExit(f"Error: No question directories (q*/) found in {base}")

    return slots, preamble_path


def validate_prerequisites(
    prerequisites: dict, slots: list[QuestionSlot]
) -> dict[int, set[int]]:
    """Validate prerequisite config and convert question names to slot indices.

    Uses Kahn's algorithm to detect cycles in the dependency graph.
    Returns a mapping from slot index to set of prerequisite slot indices.
    """
    slot_name_to_idx = {s.name: i for i, s in enumerate(slots)}
    slot_names = set(slot_name_to_idx)

    prereq_indices: dict[int, set[int]] = {}

    for question, deps in prerequisites.items():
        if question not in slot_names:
            raise SystemExit(f"Error: prerequisite key '{question}' not found in question bank")
        if not isinstance(deps, list):
            raise SystemExit(f"Error: prerequisites for '{question}' must be a list, got {type(deps).__name__}")
        for dep in deps:
            if not isinstance(dep, str):
                raise SystemExit(f"Error: prerequisite values must be strings, got {type(dep).__name__}")
            if dep not in slot_names:
                raise SystemExit(f"Error: prerequisite '{dep}' for '{question}' not found in question bank")
            if dep == question:
                raise SystemExit(f"Error: '{question}' cannot be a prerequisite of itself")

        q_idx = slot_name_to_idx[question]
        prereq_indices[q_idx] = {slot_name_to_idx[d] for d in deps}

    # Cycle detection via Kahn's algorithm (topological sort)
    in_degree: dict[int, int] = collections.defaultdict(int)
    adjacency: dict[int, list[int]] = collections.defaultdict(list)
    all_nodes: set[int] = set()

    for q_idx, dep_indices in prereq_indices.items():
        all_nodes.add(q_idx)
        for dep_idx in dep_indices:
            all_nodes.add(dep_idx)
            adjacency[dep_idx].append(q_idx)
            in_degree[q_idx] += 1

    queue = collections.deque(n for n in all_nodes if in_degree[n] == 0)
    sorted_count = 0

    while queue:
        node = queue.popleft()
        sorted_count += 1
        for neighbor in adjacency[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if sorted_count != len(all_nodes):
        raise SystemExit("Error: prerequisite graph contains a cycle")

    return prereq_indices


def is_valid_ordering(ordering: tuple[int, ...], prerequisites: dict[int, set[int]]) -> bool:
    """Check whether an ordering respects all prerequisite constraints."""
    position = {slot_idx: pos for pos, slot_idx in enumerate(ordering)}
    return all(
        all(position[dep] < position[q] for dep in deps)
        for q, deps in prerequisites.items()
    )


def distance(a: ExamAssignment, b: ExamAssignment, num_questions: int) -> int:
    """Compute weighted distance between two exam assignments.

    Variant differences are weighted by num_questions, making question content
    differences much more significant than ordering differences.
    """
    variant_diff = sum(1 for va, vb in zip(a.variant_indices, b.variant_indices) if va != vb)
    order_diff = sum(1 for oa, ob in zip(a.ordering, b.ordering) if oa != ob)
    return variant_diff * num_questions + order_diff


def generate_exam_assignments(
    slots: list[QuestionSlot],
    num_students: int,
    seed: int,
    prerequisites: dict[int, set[int]] | None = None,
) -> list[ExamAssignment]:
    """Generate num_students unique, maximally diverse exam assignments.

    Uses farthest-first traversal (greedy maximin dispersion) to select exams
    that are spread as far apart as possible in the (variant, ordering) space.
    Only orderings that respect prerequisite constraints are considered.
    """
    if prerequisites is None:
        prerequisites = {}
    num_questions = len(slots)
    variants_per_slot = [len(s.variants) for s in slots]

    # Enumerate the full exam space (only orderings that respect prerequisites)
    variant_combos = list(itertools.product(*(range(v) for v in variants_per_slot)))
    orderings = [
        o for o in itertools.permutations(range(num_questions))
        if is_valid_ordering(o, prerequisites)
    ]

    total_space = len(variant_combos) * len(orderings)

    if total_space < num_students:
        raise SystemExit(
            f"Error: Only {total_space:,} unique exams possible "
            f"({len(variant_combos):,} variant combos x {len(orderings):,} orderings), "
            f"but {num_students} requested. Add more question variants."
        )

    all_exams = [
        ExamAssignment(variant_indices=vc, ordering=o)
        for vc in variant_combos
        for o in orderings
    ]

    # Farthest-first traversal for maximum diversity
    rng = random.Random(seed)
    first_idx = rng.randrange(len(all_exams))

    selected_indices = [first_idx]
    # min_dist[i] = minimum distance from exam i to any already-selected exam
    # -1 means already selected
    min_dist = [distance(all_exams[first_idx], all_exams[i], num_questions) for i in range(len(all_exams))]
    min_dist[first_idx] = -1

    for _ in range(num_students - 1):
        best_idx = max(range(len(all_exams)), key=lambda i: min_dist[i])
        selected_indices.append(best_idx)

        # Update min distances
        new_exam = all_exams[best_idx]
        for i in range(len(all_exams)):
            if min_dist[i] >= 0:
                d = distance(new_exam, all_exams[i], num_questions)
                if d < min_dist[i]:
                    min_dist[i] = d
        min_dist[best_idx] = -1

    return [all_exams[i] for i in selected_indices]


def format_exam_id(index: int, total: int) -> str:
    """Format exam ID with zero-padding based on total count."""
    width = max(3, len(str(total)))
    return str(index + 1).zfill(width)


def render_all_exams_tex(
    assignments: list[ExamAssignment],
    config: dict,
    slots: list[QuestionSlot],
    preamble_path: str | None,
) -> str:
    """Render a single .tex file containing all exams back-to-back."""
    exam_cfg = config["exam"]
    num_students = exam_cfg["num_students"]
    lines = [r"\documentclass{ip-exam}"]

    if preamble_path is not None:
        lines.append(f"\\input{{{preamble_path}}}")

    lines.append("")
    lines.append(f"\\title{{{exam_cfg['title']} {format_exam_id(0, num_students)} -- {exam_cfg['semester']}}}")
    lines.append(f"\\examdate{{{exam_cfg['date']}}}")
    lines.append("")
    lines.append(r"\begin{document}")

    for i, assignment in enumerate(assignments):
        exam_id = format_exam_id(i, num_students)

        lines.append("")
        lines.append(f"% ===== Exam {exam_id} =====")

        if i > 0:
            lines.append(r"\cleartoeven")
            lines.append(r"\setcounter{questioncounter}{0}")
            lines.append(r"\setcounter{page}{1}")
            lines.append(
                f"\\title{{{exam_cfg['title']} {exam_id} -- {exam_cfg['semester']}}}"
            )

        lines.append(r"\makeexamheader")
        lines.append("")

        for slot_idx in assignment.ordering:
            slot = slots[slot_idx]
            variant_idx = assignment.variant_indices[slot_idx]
            variant_path = slot.variants[variant_idx]
            lines.append(f"\\input{{{variant_path}}}")

    lines.append("")
    lines.append(r"\cleartoeven")
    lines.append(r"\end{document}")
    lines.append("")

    return "\n".join(lines)


def compile_exam(tex_path: pathlib.Path, repo_root: pathlib.Path) -> None:
    """Compile a .tex file to PDF using pdflatex."""
    pdflatex = shutil.which("pdflatex")
    if pdflatex is None:
        raise SystemExit("Error: pdflatex not found in PATH")

    output_dir = tex_path.parent
    packages_dir = repo_root / "resources" / "packages"
    # TEXINPUTS: packages dir (for cls/images) + repo root (for \input paths)
    texinputs = f"{packages_dir}:{repo_root}:{os.environ.get('TEXINPUTS', '')}"
    env = {**os.environ, "TEXINPUTS": texinputs}

    # Compile from the output directory so minted cache is co-located with output
    cmd = [
        pdflatex,
        "-shell-escape",
        "-interaction=nonstopmode",
        tex_path.name,
    ]

    # Two passes: first generates minted/Pygments output, second reads it
    for pass_num in (1, 2):
        print(f"Compiling {tex_path.name} (pass {pass_num}/2)...", end=" ", flush=True)
        result = subprocess.run(
            cmd, cwd=str(output_dir), env=env, capture_output=True
        )

        stdout = result.stdout.decode("utf-8", errors="replace")
        stderr = result.stderr.decode("utf-8", errors="replace")

        if result.returncode != 0 and pass_num == 2:
            print("FAILED")
            log_path = output_dir / (tex_path.stem + ".compile.log")
            with open(log_path, "w") as f:
                f.write(stdout)
                f.write("\n--- STDERR ---\n")
                f.write(stderr)
            raise SystemExit(f"Compilation failed. See {log_path} for details.")

        print("OK")

    # Clean up auxiliary and minted cache files
    for ext in ("aux", "log", "out"):
        for f in output_dir.glob(f"*.{ext}"):
            f.unlink()
    minted_dir = output_dir / f"_minted-{tex_path.stem}"
    if minted_dir.is_dir():
        shutil.rmtree(minted_dir)


def main():
    parser = argparse.ArgumentParser(
        description="Generate unique exam variants from a question bank."
    )
    parser.add_argument("config", help="Path to TOML config file")
    parser.add_argument("--compile", action="store_true", help="Compile .tex to PDF")
    parser.add_argument("--output-dir", help="Override output directory")
    parser.add_argument(
        "--dry-run", action="store_true", help="Preview assignments without writing files"
    )
    args = parser.parse_args()

    repo_root = pathlib.Path(__file__).resolve().parent.parent

    config = load_config(args.config)
    exam_cfg = config["exam"]

    questions_dir = repo_root / "exams" / "questions"
    slots, preamble_path = scan_question_bank(questions_dir, exam_cfg["name"])

    num_students = exam_cfg["num_students"]
    seed = exam_cfg["seed"]

    prereq_cfg = config.get("prerequisites", {})
    prereq_indices = validate_prerequisites(prereq_cfg, slots)

    # Report question bank summary
    print(f"Exam: {exam_cfg['title']} -- {exam_cfg['semester']}")
    print(f"Questions: {len(slots)}")
    for slot in slots:
        print(f"  {slot.name}: {len(slot.variants)} variant(s)")
    if prereq_indices:
        print("Prerequisites:")
        for q_idx, dep_indices in prereq_indices.items():
            deps = ", ".join(slots[d].name for d in dep_indices)
            print(f"  {slots[q_idx].name} requires: {deps}")

    variants_per_slot = [len(s.variants) for s in slots]
    num_valid_orderings = sum(
        1 for o in itertools.permutations(range(len(slots)))
        if is_valid_ordering(o, prereq_indices)
    )
    total_space = math.prod(variants_per_slot) * num_valid_orderings
    print(f"Total unique exams possible: {total_space:,}")
    print(f"Generating {num_students} exams (seed={seed})...")

    assignments = generate_exam_assignments(slots, num_students, seed, prereq_indices)

    if args.output_dir:
        output_dir = pathlib.Path(args.output_dir)
    else:
        output_dir = repo_root / "exams" / "output" / exam_cfg["name"]

    if args.dry_run:
        for i, assignment in enumerate(assignments):
            exam_id = format_exam_id(i, num_students)
            print(f"\nexam {exam_id}:")
            for slot_idx in assignment.ordering:
                slot = slots[slot_idx]
                vi = assignment.variant_indices[slot_idx]
                print(f"  {slot.name}/{pathlib.Path(slot.variants[vi]).name}")
        return

    output_dir.mkdir(parents=True, exist_ok=True)

    tex_content = render_all_exams_tex(assignments, config, slots, preamble_path)
    tex_filename = f"{exam_cfg['name']}-exams.tex"
    tex_path = output_dir / tex_filename
    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(tex_content)
    print(f"Written: {tex_path}")

    if args.compile:
        compile_exam(tex_path, repo_root)

    print(f"\nDone. Output in {output_dir}/")


if __name__ == "__main__":
    main()
