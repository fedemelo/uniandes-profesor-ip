# ISIS Laboratory LaTeX Template

This LaTeX template (`isis-lab.cls`) recreates the design and layout of the ISIS laboratory documents with a professional blue color scheme and structured sections.

## Features

- **Professional Header**: Blue gradient background with course information and logo placeholder
- **Color Scheme**: Matching blue palette from the original document
- **Structured Sections**: Pre-defined environments for objectives, activities, and deliverables
- **Mathematical Formulas**: Special formatting for mathematical expressions
- **Customizable Metadata**: Easy configuration of course information

## Installation

1. Place the `isis-lab.cls` file in your LaTeX project directory
2. Use `\documentclass{isis-lab}` in your document

## Usage

### Basic Document Structure

```latex
\documentclass{isis-lab}

% Document metadata
\coursecode{ISIS-1221}
\coursename{INTRODUCCIÓN A LA PROGRAMACIÓN}
\labtype{Nivel 1}
\labnumber{Laboratorio2}
\labtitle{Descubriendo el mundo de la programación}
\headerimage{path/to/logo.png} % Optional: university logo

\begin{document}

\maketitle

% Your content here

\end{document}
```

### Available Environments

#### General Objective
```latex
\begin{objetivo}
Your general objective text here.
\end{objetivo}
```

#### Specific Objectives
```latex
\begin{objetivos}
\item First specific objective
\item Second specific objective
\item Third specific objective
\end{objetivos}
```

#### Activities
```latex
\begin{actividad}{1: Activity Name}
Activity description and instructions.
\end{actividad}
```

#### Deliverables
```latex
\begin{entrega}
Delivery instructions and requirements.
\end{entrega}
```

### Special Commands

#### Mathematical Formulas
```latex
\formula{q = mC\Delta T}
```

#### Information Boxes
```latex
\infobox{Important information or notes}
```

## Customization

### Colors
The template defines several colors that match the original document:
- `isisblue`: Main blue color for headers
- `isislightblue`: Light blue for highlights
- `isisgray`: Light gray for section backgrounds
- `isisborder`: Border color for sections

### Header Image
To add the university logo to the header, use:
```latex
\headerimage{path/to/your/logo.png}
```

If no image is provided, a placeholder `[LOGO]` will be shown.

## Requirements

The template requires the following LaTeX packages:
- `xcolor` - Color support
- `graphicx` - Image handling
- `tikz` - Graphics and header creation
- `tcolorbox` - Colored boxes for sections
- `enumitem` - Enhanced lists
- `amsmath`, `amsfonts` - Mathematical typesetting

## Example

See `sample-lab.tex` for a complete example that recreates the original document layout and content.

## Compilation

Compile with pdfLaTeX:
```bash
pdflatex sample-lab.tex
```

For best results, compile twice to ensure proper positioning of TikZ elements.
