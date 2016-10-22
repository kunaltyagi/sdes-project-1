.phony: clean all test

all: latex
	python3 automator.py
	pdflatex -output-directory=latex van_der_pol.tex
	cp van_der_pol.tex latex/
	bibtex latex/van_der_pol
	pdflatex -output-directory=latex van_der_pol.tex
	pdflatex -output-directory=latex van_der_pol.tex
	rm latex/van_der_pol.tex
	cp latex/120010006.pdf ../


latex:
	mkdir latex

clean:
	mv latex/reference.bib ./
	rm latex/* -fr
	mv reference.bib latex/
	rm figure/*.png -fr
	rm *.pyc -fr
	rm __pycache__ -fr
	rm ../*.pdf -fr

test:
	python3 -m pytest oscillator.py
