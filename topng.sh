#!/bin/bash

INPUT=$1
INPUT="${INPUT%.*}"
pdfcrop "$INPUT".pdf
mv "$INPUT"-crop.pdf "$INPUT".pdf
pdftoppm $1 $INPUT -png -rx 300 -ry 300
mv "$INPUT"-1.png "$INPUT".png
