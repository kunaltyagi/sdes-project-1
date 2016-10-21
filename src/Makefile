.phony: clean all

all: latex
	pdflatex -output-directory=latex van_der_pol.tex

latex:
	mkdir latex

clean:
	rm latex/* -fr

test:
	python3 -m pytest oscillator.py
