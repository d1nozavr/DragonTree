TARGET = src/run.py

all: run

run:
	@python3 -B -u $(TARGET)
