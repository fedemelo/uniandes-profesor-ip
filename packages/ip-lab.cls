\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{ip-lab}[2024/01/01 ISIS Laboratory Template]

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

\newcommand{\labtype}[1]{\def\@labtype{#1}}
\newcommand{\labnumber}[1]{\def\@labnumber{#1}}
\newcommand{\labtitle}[1]{\def\@labtitle{#1}}

\labtype{Nivel 1}
\labnumber{Laboratorio}
\labtitle{}

\renewcommand{\familydefault}{\sfdefault}

\newcommand{\makeheader}{
    % Fancy page style for header in first page
    \fancypagestyle{firstpage}{
        \fancyhf{}
        \fancyhead{}
        \fancyhead[C]{
            % Move header to the pages left horizontal side disregarding the margin
            % Obtained empirically
            \hspace*{-75pt}  
            % Create a box that is as wide as the page and as tall as the header
            % The header is 136pt tall (empirically obtained)
            \begin{minipage}[b][136pt]{\paperwidth}
                \includegraphics[width=\paperwidth]{ip-header.png}
            \end{minipage}%
        }
        \renewcommand{\headrulewidth}{0pt}
        \fancyfoot{}
    }
    
    % Set the page styles
    \thispagestyle{firstpage}
    \pagestyle{fancy}
    
    % Configure fancy style for subsequent pages (no header)
    \fancyhf{}
    \fancyhead{}
    \fancyfoot{}
    \renewcommand{\headrulewidth}{0pt}

    % Vertical space so content is not on top of the header
    % Obtained empirically
    \vspace*{90pt}
}

\renewcommand{\maketitle}{
    \begin{center}
        {\LARGE\bfseries \@labtype\ -- \@labnumber}\\[3pt]
        {\LARGE\bfseries\@labtitle}
    \end{center}
    
    \vspace{-20pt}
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
