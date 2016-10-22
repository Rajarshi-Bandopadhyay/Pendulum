source/153079002.pdf: source/omega.png source/theta.png source/references.bib source/references.bbl source/references.blg
	cd source && pdflatex 153079002.tex
	cd source && pdflatex 153079002.tex
	mkdir output
	mv source/153079002.pdf output/153079002.pdf

source/theta.png source/omega.png: source/images.py
	cd source && python images.py

source/references.bbl source/references.blg: source/references.bib
	cd source && pdflatex 153079002.tex
	cd source && bibtex 153079002

test: 
	python test_theory.py

.PHONY: clean

clean: 
	cd source && rm -f *.aux *.blg *.bbl *.png *.log
	rm -rf output
