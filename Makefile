# Add the `packages` directory to the `TEXINPUTS` environment variable so that pdftex can find custom packages
TEXINPUTS := ./packages/:$(TEXINPUTS)
export TEXINPUTS

# Variables
TEX=pdflatex -shell-escape
LEVEL_DIR=N4
LAB_DIR=$(LEVEL_DIR)/labs/L1
EXAM_DIR=$(LEVEL_DIR)/exam

# Rules
.PHONY: lab clean clean-all all  # Mark targets as always executed

lab:
	$(TEX) -output-directory=$(LAB_DIR) $(LAB_DIR)/n4-l1.tex

exam:
	$(TEX) -output-directory=$(EXAM_DIR) $(EXAM_DIR)/n2-exam-make-up.tex

clean:  # Remove all temporary files
	find . \( -name "*.aux" -o -name "*.log" -o -name "*.out" -o -name "*.toc" -o -name "*.pyg" \) -exec rm {} +
	find . -name "*.bak0" -exec rm {} +
	find . \( -name "*.bbl" -o -name "*.blg" \) -exec rm {} +
	find . \( -name "*.glg" -o -name "*.glo" -o -name "*.gls" -o -name "*.ist" \) -exec rm {} +
	find . \( -name "*.fdb_latexmk" -o -name "*.fls" \) -exec rm {} +
	find . \( -name "*.gz" -o -name "*.lof" -o -name "*.lot" -o -name "*.run.xml" \) -exec rm {} +

clean-all: clean  # Remove all temporary files and the generated pdf
	find . -name "*.pdf" -exec rm {} +

all: lab exam