# commitstats

visualize different statistics of commits in a git repository

### Prerequisites
- python 3 + venv module (`python3.11-venv` on Ubuntu 23)

### Usage
```sh
# Create a virtual python environment & install dependencies
python -m venv .pyenv
.pyenv/bin/pip install pandas matplotlib seaborn

# Usage example:
.pyenv/bin/python commitstats.py commits_libgcrypt.json
```
Input file format: see https://github.com/mspi21/commitfetch
