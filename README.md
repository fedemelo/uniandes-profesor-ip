# IP

Exámenes, quizzes y laboratorios que escribí como profesor del curso ISIS-1221: Introducción a la Programación de la Universidad de los Andes, entre agosto de 2025 y mayo de 2026.

Los siguientes comandos generan documentos:
- `make lab`
- `make quiz`
- `make exam`
- `make notes`

Dependen de la configuración del nivel, directorio y archivo en el Makefile. E.g., para generar el laboratorio 3 del nivel 2, es necesario modificar el Makefile cambiando `LEVEL_DIR` por 2, `LAB_DIR` por 3 y el final de la regla `lab` por `n3-l2.tex`.

El comando `make clean` elimina los archivos residuales que se autogeneran al compilar los TEX. `make clean-all` elimina además los PDFs generados.

La generación de exámenes usa un algoritmo topológico para que ningún examen tenga las mismas preguntas en el mismo orden que algún otro.
