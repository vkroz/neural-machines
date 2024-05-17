#!/usr/bin/env bash
set -x
PENV_NAME=genai_env
conda create --name ${PENV_NAME} python=3.12
source $HOME/miniconda3/etc/profile.d/conda.sh
conda activate ${PENV_NAME}
conda install pytorch torchvision torchaudio -c pytorch -y
conda install numpy pandas scikit-learn matplotlib seaborn jupyter -c conda-forge -y
conda install transformers datasets -c huggingface -y
conda install openai tiktoken -y
conda install fastapi uvicorn tqdm pytest python-dotenv boto3 -c conda-forge -y
pip install streamlit huggingface_hub
#huggingface-cli login
