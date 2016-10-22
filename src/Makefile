.phony: clean all

all: latex
	python3 automator.py
	pdflatex -output-directory=latex van_der_pol.tex

latex:
	mkdir latex

clean:
	ls latex | grep tex$ -v | sed 's/^/latex\//' | xargs rm -fr
	rm figure/*.png
	rm *.pyc -fr
	rm __pycache__ -fr

test:
	python3 -m pytest oscillator.py
