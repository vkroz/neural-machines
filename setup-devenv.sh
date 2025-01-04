#!/usr/bin/env bash
#------------------------
# First time development environment setup
# Run it once. This script will:
# 1. Create conda virtual environment
# 2. Install required packages
# 3. Generate requirements.txt for using by CI/CD pipelines with `pip install` command
#------------------------

# Create conda environment
ENV_NAME=neuman
conda create --name ${ENV_NAME} python=3.12 -y
source $HOME/miniconda3/etc/profile.d/conda.sh
conda activate ${ENV_NAME}
conda install fastapi uvicorn tqdm pytest python-dotenv boto3 -c conda-forge -y
conda install numpy pandas scikit-learn matplotlib seaborn jupyter -c conda-forge -y
conda install sqlalchemy psycopg2-binary pydantic -c conda-forge -y


# Additional packages we will need in the future
#conda install transformers datasets -c huggingface -y
#conda install pytorch torchvision torchaudio -c pytorch -y
#conda install openai tiktoken -y
#pip install streamlit

#------------------------
# Generate requirements.txt
#------------------------
PROJECT_ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )" # Find the current script directory

# List of packages to include in requirements.txt
packages=(
    "fastapi"
    "uvicorn"
    "tqdm"
    "pytest"
    "python-dotenv"
    "boto3"
    "numpy"
    "pandas"
    "scikit-learn"
    "matplotlib"
    "seaborn"
    "jupyter"
    "sqlalchemy"
    "psycopg2-binary"
    "pydantic"
)

# Create or overwrite requirements.txt in the project root
REQUIREMENTS_FILE="$PROJECT_ROOT/requirements.txt"
: > "$REQUIREMENTS_FILE"

# Use pip list to get all installed packages with versions
pip_list_output=$(pip list --format=freeze)

# Loop through each package and find its entry in pip list output
for package in "${packages[@]}"; do
    # Use grep to find the package and awk to extract the version
    version=$(echo "$pip_list_output" | grep -i "^$package==" | awk -F'==' '{print $2}')

    if [ -n "$version" ]; then
        echo "$package~=$version" >> "$REQUIREMENTS_FILE"
    else
        echo "Warning: $package not found or version not determined"
    fi
done

