# Neural Machines 

Collection of  python scripts, and notebooks for exploratory learning of LLMs, agents and AI.
Covers various prompts engineering techniques, RAG, ReAct, fine-tuning, and more.

# Setup work environment

## Prerequisites

- Miniconda https://docs.anaconda.com/miniconda/install/
- Mise package manager https://mise.jdx.dev/getting-started.html

## Setup on local machine:

1.Have miniconda installed. While we don't use conda directly, as of March 2025 it is needed to resolve build errors in hnswlib on MacOS with Apple Silicon.

2. Install virtual environment
```
# Set local Python version
mise use python@3.12

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip

# Install packages
pip install -r requirements.txt
```

# Setup GIT lfs

```
brew install git-lfs
git lfs install
```

