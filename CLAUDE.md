# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a comprehensive machine learning learning repository containing coursework, tutorials, and experimental scripts. It serves as a personal workspace for AI/ML concepts with materials from major ML programs (Coursera ML/DL specializations), quick reference tutorials, and experimentation tools.

## Environment Setup

### Primary Development Environment
```bash
# Create main environment (choose platform-specific file)
conda env create -f environment-macos.yml    # macOS
conda env create -f environment-linux.yml    # Linux
conda activate neumans

# For Coursera-specific coursework
conda env create -f learn_ml/Coursera-ML/environment-coursera_ml.yml
conda activate coursera_ml
```

### Common Development Commands
```bash
# Start Jupyter for notebook work
jupyter lab

# Test PyTorch MPS (Apple Silicon GPU) availability
python learn_ml/tools/pytorch_mps.py

# Run Streamlit demos
python learn_ml/tools/using_streamlit.py
```

## Repository Structure

### Core Learning Materials (`learn_ml/`)
- **`Coursera-ML/`** - Andrew Ng's Machine Learning specialization (classical ML, linear/logistic regression, neural networks)
- **`Coursera-DL/`** - Deep Learning specialization (neural networks, CNNs, RNNs, transformers)
- **`NLP with PyTorch/`** - PyTorch-based natural language processing tutorials
- **`d2l.ai/`** - Dive into Deep Learning textbook materials
- **`tools/`** - Utility scripts and library usage examples

### Quick Reference (`quick tutorials/`)
- **`semantic_search/`** - HNSW and bi-encoder implementations for semantic search
- **`transformers/`** - Transformer model tutorials and implementations
- **`tutorial_sqlalchemy_core.ipynb`** - Database interaction patterns

### Miscellaneous (`misc/`)
- **`backend-service-blueprint/`** - FastAPI Docker service template
- **`pii masking/`** - Data privacy and PII handling tools

## File Organization Patterns

### Coursework Structure
- **Weekly organization**: `W1/`, `W2/`, `W3/` directories for course progression
- **Assignment separation**: `W1_Assignment/` for graded work vs `W1/` for labs/exercises
- **Supporting materials**: Each week contains `data/`, `images/`, `utils.py`, `public_tests.py`
- **Naming convention**: Files prefixed with course codes (e.g., `C1_W1_Lab01_*`, `C2_W2_Assignment.ipynb`)

### Notebook Conventions
- Jupyter notebooks are the primary format for learning materials
- Rich markdown documentation with LaTeX mathematical formulas
- Self-contained examples with embedded sample data
- Progressive complexity from basic concepts to advanced implementations
- Heavy use of matplotlib/seaborn for visualization

## Technology Stack

### Core ML Libraries
- **PyTorch** (with MPS support for Apple Silicon)
- **TensorFlow/Keras**
- **scikit-learn**
- **transformers** (Hugging Face)
- **sentence-transformers**

### Data Science Tools
- **numpy, pandas** for data manipulation
- **matplotlib, seaborn, plotly** for visualization
- **Jupyter/JupyterLab** with widget extensions

### Development Tools
- **Conda** for environment management
- **Mise** for additional tooling (Python 3.12)
- **Git LFS** for large files (models, datasets)
- **Streamlit** for quick web app prototyping

## Working with This Repository

### Environment Selection
- Use `neumans` environment for general ML work and tutorials
- Use `coursera_ml` environment specifically for Coursera assignments
- Check `mise.toml` for additional tooling requirements

### Notebook Development
- Expect mathematical content with LaTeX formulas
- Large datasets may be present in course materials
- Interactive visualizations are common
- Test changes incrementally as notebooks can have long execution times

### Common Tasks
- **Reading course materials**: Navigate by course → week → specific topic
- **Running experiments**: Use `quick tutorials/` for standalone examples
- **Testing implementations**: Each assignment has `public_tests.py` for validation
- **Environment verification**: Use tools in `learn_ml/tools/` to verify setup

## Platform Considerations

- **macOS**: Use `environment-macos.yml`, PyTorch with MPS support available
- **Linux**: Use `environment-linux.yml`, CUDA support configured
- **GPU Usage**: Test with `learn_ml/tools/pytorch_mps.py` before GPU-intensive work