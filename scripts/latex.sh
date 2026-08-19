#!/usr/bin/env bash

if [ $# -ne 0 ]; then
    echo "usage: $0"
    exit
fi

python3 latex.py
cd latex
latexmk -pdf main.tex
