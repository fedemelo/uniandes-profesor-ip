\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{ip-quiz}[2024/01/01 ISIS Quiz Template]

\LoadClass[11pt,letterpaper]{article}

\RequirePackage[utf8]{inputenc}
\RequirePackage[spanish]{babel}
\RequirePackage[margin=1in]{geometry}
\RequirePackage{xcolor}
\RequirePackage{graphicx}
\RequirePackage{fancyhdr}
\RequirePackage{helvet}
\RequirePackage[T1]{fontenc}
\RequirePackage{textcase}
\RequirePackage{titlesec}
\RequirePackage{tcolorbox}
\RequirePackage{enumitem}

\definecolor{isisgray}{RGB}{236, 240, 241}

\usepackage{minted}
\setminted[python]{
  fontsize=\small,
  tabsize=4,
  breaklines=true,
  autogobble,
  style=stata-light,
}

\newcommand{\quizlevel}[1]{\def\@quizlevel{#1}}
\newcommand{\quiznum}[1]{\def\@quiznum{#1}}
\newcommand{\quiztitle}[1]{\def\@quiztitle{#1}}

\quizlevel{n1}
\quiznum{1}
\quiztitle{}

\renewcommand{\familydefault}{\sfdefault}

\newcommand{\makeheader}{
    \fancypagestyle{firstpage}{
        \fancyhf{}
        \fancyhead[C]{
            \hspace*{-75pt}
            \begin{minipage}[b][134pt]{\paperwidth}
                \includegraphics[width=\paperwidth]{ip-header-\@quizlevel.png}
            \end{minipage}%
        }
        \renewcommand{\headrulewidth}{0pt}
        \fancyfoot{}
    }
    
    \thispagestyle{firstpage}
    \pagestyle{empty}
    
    \vspace*{90pt}
}

\renewcommand{\maketitle}{
    \begin{center}
        {\LARGE\bfseries \@labtype\ -- \@labnumber}\\[3pt]
        {\LARGE\bfseries\@labtitle}
    \end{center}
    
    \vspace{-20pt}
}

\newcommand{\response}[1][10cm]{%
    \vspace{10pt}
    \noindent\textbf{Respuesta:}
    \vspace{5pt}
    \hrule
    \vspace{#1}
    \hrule
}

\setlength{\parindent}{0pt}
\setlength{\parskip}{6pt plus 2pt minus 1pt}

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

\setlist[enumerate]{
    leftmargin=20pt,
    itemsep=3pt,
    parsep=0pt,
    topsep=5pt
}

\setlength{\textfloatsep}{10pt}
\setlength{\intextsep}{10pt}
\setlength{\parindent}{0pt}

\setlength{\topskip}{10pt}
\raggedbottom
\setlength{\parskip}{6pt plus 2pt minus 1pt}

\newenvironment{sectionbox}[1]{%
    \vspace{-20pt}
    \section{\LARGE\bfseries #1}
    \vspace{-30pt}
}

\endinput

