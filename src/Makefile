
##
# @file Makefile
# @author Matúš Csirik (xcsirim00)
# @date April 8, 2024
# @todo  Bude-li to možné, Makefile nebude obsahovat jméno ani jednoho ze zdrojových souborů.
##

.PHONY: all pack clean run profile help setup setup_tests test doc
TEST_FILES = mathlib_tests.py profiling_tests.py

# Start the program
all: setup run profile
	@echo "Starting the program..."

# Copies the entire directory for now
pack: clean setup doc
	@echo "Packing the project..."
	mkdir -p ../xcsirim00_xgajduv00_xlajdat00_xvalapm00
	mkdir ../xcsirim00_xgajduv00_xlajdat00_xvalapm00/doc
	cp -pr ../doc ../../xcsirim00_xgajduv00_xlajdat00_xvalapm00/doc
	mkdir ../xcsirim00_xgajduv00_xlajdat00_xvalapm00/repo
	git clone --mirror . ../xcsirim00_xgajduv00_xlajdat00_xvalapm00/repo
	#	cp installer.py ../xcsirim00_xgajduv00_xlajdat00_xvalapm00/
	#	cp uninstaller.py ../xcsirim00_xgajduv00_xlajdat00_xvalapm00/
	zip -r xcsirim00_xgajduv00_xlajdat00_xvalapm00.zip ../../xcsirim00_xgajduv00_xlajdat00_xvalapm00/

clean:
	@echo "Cleaning up..."
	rm -rf ../doc
	rm -f xcsirim00_xgajduv00_xlajdat00_xvalapm00.zip
	rm -f installer.zip
	rm -rf __pycache__
	rm -rf dist
	rm -rf build
	rm -f *.spec
	rm -rf ../installer/Kalkulajda
	if [ -f "../installer/Kalkulajda.deb" ]; then rm ../installer/Kalkulajda.deb; fi
	if [ -f "calculator" ]; then rm calculator; fi
	if [ -f "profiling" ]; then rm profiling; fi

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
	@echo "make install - Sets up installation zip package."
	@echo "If make is run without specifying a target, make all is executed."

test:
	@echo "Running tests..."
	pytest $(TEST_FILES)

doc: Doxyfile
	rm -rf ../doc
	mkdir ../doc
	doxygen Doxyfile
	mv ../html/ ../doc
	rm -rf ../latex/

setup:
	@echo "Setting up the project..."
	sudo apt-get update
	sudo apt-get install python3-pip
	sudo apt-get install python3-tk
	sudo apt-get install tk-dev
	pip3 install -r requirements.txt

# Doesnt work yet
setup_tests:
	@echo "Setting up the project for testing..."
	pip3 install -r requirements_tests.txt

# Setup the installation zip file
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
