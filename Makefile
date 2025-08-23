# Add the `packages` directory to the `TEXINPUTS` environment variable so that pdftex can find custom packages
TEXINPUTS := ./packages/:$(TEXINPUTS)
export TEXINPUTS

# Variables
TEX=pdflatex -shell-escape
N1_DIR=N1
OUTPUT_DIR=$(N1_DIR)
LABS_DIR=$(N1_DIR)/labs
EXAM_DIR=$(N1_DIR)/exam

# Rules
.PHONY: n1-l2 clean clean-all all  # Mark targets as always executed

n1-l2:
	$(TEX) -output-directory=$(LABS_DIR) $(LABS_DIR)/n1-l2.tex

clean:  # Remove all temporary files
	find . \( -name "*.aux" -o -name "*.log" -o -name "*.out" -o -name "*.toc" -o -name "*.pyg" \) -exec rm {} +
	find . -name "*.bak0" -exec rm {} +
	find . \( -name "*.bbl" -o -name "*.blg" \) -exec rm {} +
	find . \( -name "*.glg" -o -name "*.glo" -o -name "*.gls" -o -name "*.ist" \) -exec rm {} +
	find . \( -name "*.fdb_latexmk" -o -name "*.fls" \) -exec rm {} +
	find . \( -name "*.gz" -o -name "*.lof" -o -name "*.lot" -o -name "*.run.xml" \) -exec rm {} +

clean-all: clean  # Remove all temporary files and the generated pdf
	find . -name "*.pdf" -exec rm {} +

all: n1-l2