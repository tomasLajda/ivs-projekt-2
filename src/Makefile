##
# @file Makefile
# @author Matúš Csirik (xcsirim00)
# @date April 8, 2024
##

.PHONY: all pack clean run profile help setup test doc install
DIR = ../../xcsirim00_xgajduv00_xlajdat00_xvalapm00

# Start the program
all: setup

pack: clean install doc
	@echo "Packing the project..."
	mkdir -p $(DIR)/doc $(DIR)/repo $(DIR)/install
	cp -r doc $(DIR)
	cd .. && git clone . ../xcsirim00_xgajduv00_xlajdat00_xvalapm00/repo && cd src
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

profile: setup profiling.py
	@echo "Running the profiling script..."
	python3 profiling.py

generate_profiling_data: generate_profiling_data.py
	@echo "Generating profiling data..."
	python3 generate_profiling_data.py

profile_stats: profiling.py print_profiling_stats.py
	@echo "Running the profiling script and generating stats..."
	python3 -m cProfile -o ../profiling/test.profile profiling.py
	python3 print_profiling_stats.py ../profiling/test.profile > ../profiling/profile_stats_test.txt
	@echo "Profiling data saved to profiling/test.profile"
	snakeviz ../profiling/test.profile

help:
	@echo "Makefile options:"
	@echo "make all - Downloads all dependencies and sets up the project."
	@echo "make pack - Packs the project for submission. (Local directory: $(DIR))"
	@echo "make clean - Deletes all files that should not be submitted."
	@echo "make test - Runs all tests."
	@echo "make doc - Generates project documentation."
	@echo "make run - Runs calculator program."
	@echo "make profile - Runs the standard deviation calculation program for profiling."
	@echo "make setup - Downloads all dependencies and sets up the project."
	@echo "make install - Sets up installation zip package."
	@echo "If make is run without specifying a target, make all is executed."

test:
	@echo "Running all tests..."
	pytest tests.py

doc: Doxyfile
	rm -rf ../doc
	doxygen Doxyfile

setup:
	@if [ `id -u` -ne 0 ]; then \
		echo "Please run with sudo."; \
		exit 1; \
	fi
	@echo "Setting up the project..."
	apt-get install python3-pip
	apt-get install python3-tk
	apt-get install tk-dev
	apt-get install doxygen
	apt-get install graphviz
	pip3 install -r requirements.txt

# Setup the installation zip file and clean after itself
install: setup calculator.py help_menu.py mathlib.py profiling.py
	@echo "Setting up the installer..."
	cp Pictures ../installer -r
	pyinstaller --onefile --hidden-import=PIL._tkinter_finder --hidden-import=_tkinter --hidden-import=PIL --hidden-import=tkinter --add-data 'Pictures/*:Pictures' calculator.py mathlib.py help_menu.py
	pyinstaller --onefile profiling.py mathlib.py
	mv dist/calculator ../installer
	mv dist/profiling ../installer
	rm -rf dist
	rm -rf build
	rm -f *.spec
	rm -rf ../installer/Kalkulajda
	if [ -f "../installer/Kalkulajda.deb" ]; then rm ../installer/Kalkulajda.deb; fi
	if [ -f "calculator" ]; then rm calculator; fi
	if [ -f "profiling" ]; then rm profiling; fi
	zip -r installer.zip ../installer/*
	@echo "installer.zip created."
