# Add `packages` directory to `TEXINPUTS` env var so pdftex can find custom packages
# Directory is relative, so it looks for a packages/ directory 
# within the directory where the tex file being compiled is located.
TEXINPUTS := ./packages/:$(TEXINPUTS)
export TEXINPUTS

TEX=pdflatex -shell-escape
LEVEL_DIR=n2
LAB_DIR=$(LEVEL_DIR)/labs/l1
EXAM_DIR=$(LEVEL_DIR)/exam
QUIZ_DIR=$(LEVEL_DIR)/quizzes/q3
RESOURCES_DIR=resources
NOTES_DIR=notes

.PHONY: lab quiz exam clean notes clean-all all generate-exams generate-exams-pdf generate-exams-dry clean-exams

lab:
	cd $(RESOURCES_DIR) && $(TEX) -output-directory=$(LAB_DIR) $(LAB_DIR)/n2-l1.tex

quiz:
	cd $(RESOURCES_DIR)/$(QUIZ_DIR) && TEXINPUTS=../../../packages/:$(TEXINPUTS) $(TEX) n2-q3-1.tex

exam:
	cd $(RESOURCES_DIR) && cd $(NOTES_DIR) && $(TEX) -output-directory=$(EXAM_DIR) $(EXAM_DIR)/n2-exam-make-up.tex

notes:
	cd $(NOTES_DIR) && $(TEX) ip.tex

clean:  # Remove all temporary files
	find . \( -name "*.aux" -o -name "*.log" -o -name "*.out" -o -name "*.toc" -o -name "*.pyg" \) -exec rm {} +
	find . -name "*.bak0" -exec rm {} +
	find . \( -name "*.bbl" -o -name "*.blg" \) -exec rm {} +
	find . \( -name "*.glg" -o -name "*.glo" -o -name "*.gls" -o -name "*.ist" \) -exec rm {} +
	find . \( -name "*.fdb_latexmk" -o -name "*.fls" \) -exec rm {} +
	find . \( -name "*.gz" -o -name "*.lof" -o -name "*.lot" -o -name "*.run.xml" \) -exec rm {} +

clean-all: clean  # Remove all temporary files and the generated pdf
	find . -name "*.pdf" -exec rm {} +

all: lab exam

# Exam generation
EXAM_CONFIG ?= exams/config/n1-exam.toml

generate-exams:
	python3 exams/generate.py $(EXAM_CONFIG)

generate-exams-pdf:
	python3 exams/generate.py $(EXAM_CONFIG) --compile

generate-exams-dry:
	python3 exams/generate.py $(EXAM_CONFIG) --dry-run

clean-exams:
	rm -rf exams/output/