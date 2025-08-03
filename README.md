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

### Mananging conda environments

Create from scratch
```
conda create -n neumans python=3.10
conda activate neumans

conda install -c conda-forge transformers datasets -y
conda install -c conda-forge scikit-learn -y
conda install -c conda-forge jupyter matplotlib seaborn plotly -y
conda install sentencepiece protobuf -y
pip install torch torchvision
pip install hnswlib
```

Save config file from current environment
```
conda env export > environment-macos.yml
```

## Work with GPU

### Verify MPS (Metal Performance Shaders) Support

```python
import torch

print(f"PyTorch version: {torch.__version__}")

# Check MPS availability
if torch.backends.mps.is_available():
    print("✅ MPS (Apple Silicon GPU) available: True")
    device = torch.device("mps")
    print(f"Using device: {device}")
else:
    print("❌ MPS not available")
    device = torch.device("cpu")

# Test with a simple tensor
x = torch.randn(3, 3).to(device)
print(f"Tensor on {device}: {x}")
```

### Using M3 Max GPU

```python
import torch
import torch.nn as nn

# Your M3 Max has 40 GPU cores - excellent for deep learning!
if torch.backends.mps.is_available():
    device = torch.device("mps")
    print("�� Using Apple M3 Max GPU (40 cores)")
else:
    device = torch.device("cpu")
    print("Using CPU")

# Example neural network
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(10, 20)
        self.fc2 = nn.Linear(20, 1)
    
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# Move model to GPU
model = SimpleNN().to(device)
print(f"Model moved to: {next(model.parameters()).device}")

# Test with data
data = torch.randn(100, 10).to(device)
output = model(data)
print(f"Output shape: {output.shape}")
print(f"Output device: {output.device}")
```