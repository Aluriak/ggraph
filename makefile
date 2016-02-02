PYTHON=python3
PORT = 8080
OPTIONS=$(PORT) True

run:
	$(PYTHON) -m ggraph $(OPTIONS)

all:
	python -m ggraph 8080 True
