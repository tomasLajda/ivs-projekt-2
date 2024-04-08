##
# @file Makefile
# @author Matúš Csirik (xcsirim00)
# @date April 8, 2024
##

.PHONY: all pack clean run profile help
TEST_FILES = mathlib_tests.py profiling_tests.py

# Start the program
all: setup run profile
	@echo "Starting the program..."

pack: clean setup doc
	@echo "Packing the project..."
	mkdir -p ../xcsirim00_xgajduv00_xlajdat00_xvalapm00
	cp -r . ../xcsirim00_xgajduv00_xlajdat00_xvalapm00/
	git archive --format zip --output ../xcsirim00_xgajduv00_xlajdat00_xvalapm00.zip HEAD
	cp installer.py ../xcsirim00_xgajduv00_xlajdat00_xvalapm00/
	cp uninstaller.py ../xcsirim00_xgajduv00_xlajdat00_xvalapm00/
	cp -r ../doc ../xcsirim00_xgajduv00_xlajdat00_xvalapm00/
	zip -r xcsirim00_xgajduv00_xlajdat00_xvalapm00.zip ../xcsirim00_xgajduv00_xlajdat00_xvalapm00/

clean:
	@echo "Cleaning up..."
	rm -rf ../doc

run:
	@echo "Running the program..."
	python3 calculator.py

profile: setup
	@echo "Profiling the program..."
	python3 profiling.py

help:
	@echo "Makefile options:"
	@echo "make all - Compiles the project, including the profiling program."
	@echo "make pack - Packs the project for submission."
	@echo "make clean - Deletes all files that should not be submitted."
	@echo "make test - Runs the tests for the math library."
	@echo "make doc - Generates project documentation."
	@echo "make run - Runs calculator program."
	@echo "make profile - Compiles the standard deviation calculation program for profiling."
	@echo "make setup - Sets up the necessary dependencies for the project."
	@echo "make setup_tests - Sets up the necessary dependencies for the project tests."
	@echo "If make is run without specifying a target, make all is executed."

test:
	@echo "Running tests..."
	pytest $(TEST_FILES)

doc: Doxyfile
	rm -rf ../doc
	mkdir ../doc
	doxygen Doxyfile

setup:
	@echo "Setting up the project..."
	pip3 install -r requirements.txt

setup_tests:
	@echo "Setting up the project for testing..."
	pip3 install -r requirements_tests.txt
