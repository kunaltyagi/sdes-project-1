.phony: clean all test

all:
	make all -C src

clean:
	make clean -C src

test:
	make test -C src
