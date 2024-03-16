CURRENT_PATH=$(shell pwd)

all: run
.PHONY: all


run: 
	@echo
	python3 -V
	@echo
	@echo "***************** RUNNING PYTHON SCRIPT AT ${CURRENT_PATH}/src *****************"
	@echo
	python3 -u ./src/script.py
	@echo
	@echo

