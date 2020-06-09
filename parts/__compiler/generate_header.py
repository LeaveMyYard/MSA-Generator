#! /usr/bin/env python
# -*- coding: utf-8 -*-

import settings

print(
    r"""\documentclass[12pt]{article}
\usepackage{amsfonts}        
\usepackage[T2A]{fontenc}    
\usepackage[utf8]{inputenc}  
\usepackage[russian]{babel}  
\usepackage{amsmath}
\usepackage{graphicx}        
\usepackage{lscape}
\usepackage{pdflscape}
\usepackage{pdfpages}
\usepackage{hyperref}        
\usepackage{hyphenat}        
\usepackage{listings}        
\usepackage{color}
\usepackage{float}
\usepackage{comment}

\usepackage{rotating}
\usepackage{geometry}
 \geometry{
 a4paper,
 total={170mm,257mm},
 left=20mm,
 top=20mm,
 }


\graphicspath{./}

\definecolor{dkgreen}{rgb}{0,0.6,0}
\definecolor{gray}{rgb}{0.5,0.5,0.5}
\definecolor{mauve}{rgb}{0.58,0,0.82}

\newcommand{\bigcell}[2]{\begin{tabular}{@{}#1@{}}#2\end{tabular}}
\newcommand{\me}{\mathrm{e}}

\addto\captionsrussian{\renewcommand{\contentsname}{Зміст}}

\lstset{
  frame=none,
  language=Python,
  aboveskip=3mm,
  belowskip=3mm,
  showstringspaces=false,
  columns=flexible,
  basicstyle={\small\ttfamily},
  numbers=none,
  numberstyle=\tiny\color{gray},
  keywordstyle=\color{blue},
  commentstyle=\color{dkgreen},
  stringstyle=\color{mauve},
  breaklines=true,
  breakatwhitespace=true,
  tabsize=3
}

\setcounter{tocdepth}{3} %%where n is the level, starting with 0(chapters only)


\begin{document}

\begin{center}
\large{Одеський національний університет імені І.І.Мечникова
    \newline
Факультет математики, фізики та інформаційних технологій
    \newline
}
\bigbreak
\bigbreak
\bigbreak
\bigbreak
\bigbreak
\bigbreak
\bigbreak
\bigbreak
\\
\\
\\
\\
\bigbreak
\LARGE{ \textbf{Лабораторна робота}
\bigbreak
\textbf{Варіант """
    + str(settings.variant)
    + r"""}
\bigbreak

\bigbreak
}
\end{center}
\bigbreak
\bigbreak
\bigbreak
\bigbreak
\begin{flushright}
\large{Звіт студента ІІІ курсу
\bigbreak
денної форми навчання
\bigbreak
спеціальності
\bigbreak
113 Прикладна математика
\bigbreak
"""
    + settings.name
    + r"""
\bigbreak
\begin{center}

  \bigbreak
  \
  \bigbreak
  \
  \bigbreak
  \
  \bigbreak
  \
  \LARGE{ {}
  \
\bigbreak
\
\bigbreak
}
                  2020

\end{center}
}
\end{flushright}

\newpage"""
)
