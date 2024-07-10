#!/usr/bin/env bash
#------------------------
# First time development environment setup
# Run it once. This script will:
# 1. Create conda virtual environment
# 2. Install required packages
# 3. Generate requirements.txt for using by CI/CD pipelines with `pip install` command
#------------------------

# Function to find the project root (assumes the script is in ./scripts)
find_project_root() {
    local current_dir="$PWD"
    while [[ "$current_dir" != "/" ]]; do
        if [[ -d "$current_dir/scripts" ]]; then
            echo "$current_dir"
            return 0
        fi
        current_dir="$(dirname "$current_dir")"
    done
    echo "Error: Unable to find project root" >&2
    return 1
}

# Find the project root
PROJECT_ROOT=$(find_project_root)
if [[ $? -ne 0 ]]; then
    exit 1
fi

# Create conda environment
ENV_NAME=neuman
conda create --name ${ENV_NAME} python=3.12 -y
source $HOME/miniconda3/etc/profile.d/conda.sh
conda activate ${ENV_NAME}
conda install fastapi uvicorn tqdm pytest python-dotenv boto3 -c conda-forge -y
conda install numpy pandas scikit-learn matplotlib seaborn jupyter -c conda-forge -y

# Additional packages we will need in the future
#conda install transformers datasets -c huggingface -y
#conda install pytorch torchvision torchaudio -c pytorch -y
#conda install openai tiktoken -y
#pip install streamlit

#------------------------
# Generate requirements.txt
#------------------------

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

