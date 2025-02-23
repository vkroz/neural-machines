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

### Configure virtual environment
```
conda create -n neumans python=3.10
conda activate neumans

conda install -c conda-forge pytorch
conda install -c conda-forge transformers
conda install -c conda-forge datasets
conda install -c conda-forge pandas
conda install -c conda-forge pyarrow
conda install -c conda-forge scikit-learn
conda install -c conda-forge sentencepiece protobuf hnswlib
conda install -c conda-forge jupyter matplotlib seaborn plotly
```

### Activate virtual environment

```
conda activate neumans
```




