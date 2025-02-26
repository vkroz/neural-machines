# Neural Machines 

Collection of  python scripts, and notebooks for exploratory learning of LLMs, agents and AI.
Covers various prompts engineering techniques, RAG, ReAct, fine-tuning, and more.

# Setup work environment

## Prerequisites

- Miniconda https://docs.anaconda.com/miniconda/install/
- Mise package manager https://mise.jdx.dev/getting-started.html

## Setup on local machine:

### Prerequisites
1. Have miniconda installed
```
curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh
bash ./Miniconda3-latest-MacOSX-arm64.sh
rm ./Miniconda3-latest-MacOSX-arm64.sh
```

2. Setup GIT lfs
```
brew install git-lfs
git lfs install
```

### Use virtual environment

Create from config file
```
# For MacOS
conda env create -f environment-macos.yml

# For Linux
conda env create -f environment-linux.yml
```

Activate to use
```
conda activate neumans
```

### Sync to remote server

```
./sync_to_remote.sh
```

### To create conda env from scratch manually

```
conda create -n neumans python=3.10
conda activate neumans

conda install -c pytorch pytorch torchvision -y
conda install -c conda-forge transformers datasets -y
conda install -c conda-forge scikit-learn -y
conda install -c conda-forge jupyter matplotlib seaborn plotly -y
conda install sentencepiece protobuf -y
pip install hnswlib
```