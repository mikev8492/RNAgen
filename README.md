# RNAgen DEMO

## Description:

Streamlit web interface for [RNAgen](https://github.com/mikev8492/RNAgen) 

### UI Features

- **Parameter controls** — configure all sequence generation settings from the sidebar using sliders and number inputs
- **Instant download** — generated sequences are available as a `.fasta` file with one click, no output path required
- **Sequence preview** — each sequence is displayed in an expandable panel showing GC content, ambiguity content, ORF type, and flanking status
- **Summary metrics** — after generation, a dashboard displays total sequences, complete ORF count, flanked count, and average length

### Live Demo

The hosted version is available at [rna-gen.streamlit.app](https://rna-gen.streamlit.app/).


## Requirements:
- Python 3.11 or later
- Conda (Anaconda or Miniconda)
- streamlit

### Required packages:
- numpy
- biopython

## Project Structure:
```
└── 📁RNAgen_demo
    └── 📁output
    └── 📁src
        ├── __init__.py
        ├── sequence_lib.py
        ├── simulator.py
    ├── app.py
    ├── main.py
    ├── environment.yml
    ├── LICENSE
    ├── pseudocode.txt
    ├── README.md
    └── requirements.txt
```

- `main.py`: CLI entry point

- `app.py`: Web UI entry point

- `src/simulator.py`: Core simulation logic

- `src/sequence_lib.py`: Utility functions

## Installation:

### 1. Clone the repository
```bash
git clone https://github.com/mikev8492/RNAgen.git

cd RNAgen
```
### 2. Create conda environment
```bash
conda env create -f environment.yml

conda activate RNAgen_demo
```
### 3. Run the UI

```bash
streamlit run app.py
```

## License:
GNU GENERAL PUBLIC LICENSE

## Author:
Michael Villarreal - mvillar6@charlotte.edu | mikev8492@gmail.com
