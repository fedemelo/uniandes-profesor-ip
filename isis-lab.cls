\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{isis-lab}[2024/01/01 ISIS Laboratory Template]

% Base class
\LoadClass[11pt,letterpaper]{article}

\RequirePackage[utf8]{inputenc}
\RequirePackage[spanish]{babel}
\RequirePackage[margin=1in]{geometry}
\RequirePackage{xcolor}
\RequirePackage{graphicx}
\RequirePackage{tikz}
\RequirePackage{enumitem}
\RequirePackage{array}
\RequirePackage{tabularx}
\RequirePackage{amsmath}
\RequirePackage{amsfonts}
\RequirePackage{fancyhdr}
\RequirePackage{titlesec}
\RequirePackage{tcolorbox}
\RequirePackage{multicol}
\RequirePackage{calc}
\RequirePackage{helvet}
\RequirePackage[T1]{fontenc}

\definecolor{isisblue}{RGB}{52, 152, 219}
\definecolor{isislightblue}{RGB}{174, 214, 241}
\definecolor{isisgray}{RGB}{236, 240, 241}
\definecolor{isisdarkgray}{RGB}{149, 165, 166}

\newcommand{\coursecode}[1]{\def\@coursecode{#1}}
\newcommand{\coursename}[1]{\def\@coursename{#1}}
\newcommand{\labtype}[1]{\def\@labtype{#1}}
\newcommand{\labnumber}[1]{\def\@labnumber{#1}}
\newcommand{\labtitle}[1]{\def\@labtitle{#1}}
\newcommand{\headerimage}[1]{\def\@headerimage{#1}}

% Default values
\coursecode{ISIS-1221}
\coursename{INTRODUCCIÓN A LA PROGRAMACIÓN}
\labtype{Nivel 1}
\labnumber{Laboratorio}
\labtitle{}
\headerimage{}

\renewcommand{\familydefault}{\sfdefault}

\renewcommand{\maketitle}{
    \begin{center}
        {\LARGE\bfseries \@labtype\ -- \@labnumber}\\[3pt]
        {\LARGE\bfseries\@labtitle}
    \end{center}
    
    \vspace{-8pt}
}

\titleformat{\section}
    {\large\bfseries}
    {}
    {0pt}
    {\colorsection}

\newcommand{\colorsection}[1]{%
    \begin{tcolorbox}[
        colback=isisgray,
        colframe=black,
        boxrule=0pt,
        bottomrule=1pt,
        rightrule=1pt,
        arc=0pt,
        left=0pt,
        right=0pt,
        top=1pt,
        bottom=0pt
    ]
        #1
    \end{tcolorbox}
}

\newenvironment{sectionbox}[1][Objetivo general]{%
    \vspace{-20pt}
    \section{\LARGE\bfseries #1}
    \vspace{-20pt}
}{}

\setlist[enumerate]{
    leftmargin=20pt,
    itemsep=3pt,
    parsep=0pt,
    topsep=5pt
}

\setlength{\textfloatsep}{10pt}
\setlength{\intextsep}{10pt}

\endinput
