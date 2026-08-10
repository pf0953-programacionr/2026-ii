#!/bin/bash
# Genera el programa del curso en DOCX y PDF a partir de programa.md.
#
# Flujo: programa.md (fuente de la verdad)
#   1. pandoc (gfm -> html): resuelve las tablas con <br> en las celdas.
#   2. pandoc (html -> docx) con referencia.docx como documento de
#      referencia (estilos, márgenes y encabezados con los logos de la
#      UCR y del SEP). Si referencia.docx no existe, se genera con
#      generar-referencia.py.
#   3. postprocesar.py: ajustes de formato al DOCX.
#   4. LibreOffice (docx -> pdf).
#
# Uso: ./generar.sh

set -euo pipefail
cd "$(dirname "$0")"

PANDOC="${PANDOC:-$HOME/miniconda3/bin/pandoc}"
REFERENCIA="referencia.docx"
SALIDA="pf0953-programacionr-g001-2026-ii"

[ -f "$REFERENCIA" ] || python3 generar-referencia.py

"$PANDOC" programa.md -f gfm -t html -o /tmp/programa-tmp.html
"$PANDOC" /tmp/programa-tmp.html -f html -o "$SALIDA.docx" --reference-doc="$REFERENCIA"
python3 postprocesar.py "$SALIDA.docx"

libreoffice --headless --convert-to pdf --outdir . "$SALIDA.docx" > /dev/null

echo "Generados: $SALIDA.docx y $SALIDA.pdf"
