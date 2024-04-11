
##
# @file Makefile
# @author Matúš Csirik (xcsirim00)
# @date April 8, 2024
# @todo  Bude-li to možné, Makefile nebude obsahovat jméno ani jednoho ze zdrojových souborů.
##

.PHONY: all pack clean run profile help setup test test_lib test_prof doc install
DIR = ../../xcsirim00_xgajduv00_xlajdat00_xvalapm00

# Start the program
all: setup run profile
	@echo "Starting the program..."

pack: clean install doc
	@echo "Packing the project..."
	mkdir -p $(DIR)/doc $(DIR)/repo $(DIR)/install
	cp -r doc $(DIR)
	cd .. && git clone --mirror . $(DIR)/repo && cd src
	cp installer.zip $(DIR)/install
	zip -r $(DIR).zip $(DIR)

clean:
	@echo "Cleaning up..."
	rm -rf ../doc
	rm -f $(DIR).zip
	rm -rf $(DIR)
	rm -f installer.zip
	rm -rf __pycache__

run: calculator.py
	@echo "Running the calculator..."
	python3 $<

profile: profiling.py setup
	@echo "Running the profiling script..."
	python3 $<

help:
	@echo "Makefile options:"
	@echo "make all - Compiles the project, including the profiling program."
	@echo "make pack - Packs the project for submission. (Local directory: $(DIR))"
	@echo "make clean - Deletes all files that should not be submitted."
	@echo "make test - Runs all tests."
	@echo "make test_lib - Runs the tests for the math library."
	@echo "make test_prof - Runs the tests for the profiling function."
	@echo "make doc - Generates project documentation."
	@echo "make run - Runs calculator program."
	@echo "make profile - Compiles the standard deviation calculation program for profiling."
	@echo "make setup - Sets up the necessary dependencies for the project."
	@echo "make setup_tests - Sets up the necessary dependencies for the project tests."
	@echo "make install - Sets up installation zip package."
	@echo "If make is run without specifying a target, make all is executed."

test:
	@echo "Running all tests..."
	pytest *_tests.py

test_lib:
	@echo "Running math library tests..."
	pytest mathlib_tests.py

test_prof:
	@echo "Running profiling tests..."
	pytest profiling_tests.py

doc: Doxyfile
	rm -rf doc
	mkdir doc
	doxygen $<
	mv html doc
	rm -rf latex

setup:
	@echo "Setting up the project..."
	sudo apt-get update
	sudo apt-get install python3-pip
	sudo apt-get install python3-tk
	sudo apt-get install tk-dev
	pip3 install -r requirements.txt

# Setup the installation zip file and clean after itself
install: setup calculator.py help_menu.py mathlib.py profiling.py
	@echo "Setting up the installer..."
	pyinstaller --onefile --hidden-import=PIL._tkinter_finder --hidden-import=_tkinter --hidden-import=PIL --hidden-import=tkinter --add-data 'Pictures/Calculator_30001 (1).png':Pictures calculator.py mathlib.py help_menu.py
	pyinstaller --onefile --hidden-import=PIL._tkinter_finder --hidden-import=_tkinter --hidden-import=PIL --hidden-import=tkinter --add-data 'Pictures/Calculator_30001 (1).png':Pictures profiling.py mathlib.py
	mv dist/calculator ../installer
	mv dist/profiling ../installer
	rm -rf dist
	rm -rf build
	rm -f *.spec
	rm -rf ../installer/Kalkulajda
	if [ -f "../installer/Kalkulajda.deb" ]; then rm ../installer/Kalkulajda.deb; fi
	if [ -f "calculator" ]; then rm calculator; fi
	if [ -f "profiling" ]; then rm profiling; fi
	@echo "installer.zip created."
	zip -r installer.zip ../installer/*
