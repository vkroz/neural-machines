"""
Semantic Matching Service for e-Commerce

This script implements a bi-encoder model for semantic search in e-commerce applications.
It uses the ESCI dataset which includes queries and products with relevance labels.

Architecture:
- Two-tower architecture with bi-encoder models
- Query encoder and product encoder
- Contrastive learning approach

Dataset: https://huggingface.co/datasets/Studeni/amazon-esci-data
"""

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from transformers import AutoTokenizer, AutoModel
import pandas as pd
from datasets import load_dataset
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Configuration
config = {
    'model_name': 'distilbert-base-uncased',  # Lightweight distilled model for semantic search
    'batch_size': 32, 
    'epochs': 2,
    'learning_rate': 2e-3,
    'max_length': 128
}

# BiEncoder Model
class BiEncoder(nn.Module):
    def __init__(self, model_name):
        super().__init__()
        self.query_encoder = AutoModel.from_pretrained(model_name)
        self.product_encoder = AutoModel.from_pretrained(model_name)
        self.projection = nn.Linear(self.query_encoder.config.hidden_size, 256)  # Project to smaller embedding size
        
    def encode_query(self, query_inputs):
        outputs = self.query_encoder(**query_inputs)
        cls_embedding = outputs.last_hidden_state[:, 0, :]
        return self.projection(cls_embedding)
        
    def encode_product(self, product_inputs):
        outputs = self.product_encoder(**product_inputs)
        cls_embedding = outputs.last_hidden_state[:, 0, :]
        return self.projection(cls_embedding)
        
    def forward(self, query_inputs, product_inputs):
        query_emb = self.encode_query(query_inputs)
        product_emb = self.encode_product(product_inputs)
        return query_emb, product_emb

# Dataset class
class AmazonESCIDataset(Dataset):
    def __init__(self, queries_df, products_df, tokenizer, max_length=128):
        self.queries = queries_df
        self.products = products_df
        self.tokenizer = tokenizer
        self.max_length = max_length
        self.label_map = {'Exact': 1.0, 'Substitute': 0.8, 'Complement': 0.3, 'Irrelevant': 0.0}
        
    def __len__(self):
        return len(self.queries)
    
    def __getitem__(self, idx):
        row = self.queries.iloc[idx]
        query = row['query']
        product_id = row['product_id']
        
        # Get product information
        product = self.products[self.products['product_id'] == product_id].iloc[0]
        
        # Handle missing values safely
        def safe_get(field):
            value = product[field]
            return value if isinstance(value, str) else ''
            
        product_text = (
            "Title: " + safe_get('product_title') + "; " +
            "Description: " + safe_get('product_description') + "; " +
            "Bullet Points: " + safe_get('product_bullet_point')
        )
        
        # Tokenize inputs
        query_inputs = self.tokenizer(
            query, 
            max_length=self.max_length, 
            padding='max_length', 
            truncation=True, 
            return_tensors='pt'
        )
        
        product_inputs = self.tokenizer(
            product_text,
            max_length=self.max_length,
            padding='max_length',
            truncation=True,
            return_tensors='pt'
        )
        
        label = torch.tensor(self.label_map[row['esci_label']], dtype=torch.float)
        
        return {
            'query_inputs': {k: v.squeeze(0) for k, v in query_inputs.items()},
            'product_inputs': {k: v.squeeze(0) for k, v in product_inputs.items()},
            'label': label
        }

# Training Function
def train_epoch(epoch: int, model: BiEncoder, dataloader: DataLoader, optimizer: torch.optim.AdamW, criterion: nn.MSELoss, device: torch.device) -> float:
    logger.info(f"Training epoch {epoch + 1}...")
    model.train()
    total_loss = 0
    
    for batch in dataloader:
        optimizer.zero_grad()
        
        query_inputs = {k: v.to(device) for k, v in batch['query_inputs'].items()}
        product_inputs = {k: v.to(device) for k, v in batch['product_inputs'].items()}
        labels = batch['label'].to(device)
        
        query_emb, product_emb = model(query_inputs, product_inputs)
        cos_sim = torch.nn.functional.cosine_similarity(query_emb, product_emb)
        loss = criterion(cos_sim, labels)
        
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    
    return total_loss / len(dataloader)

def load_and_prepare_data():
    """Load and prepare the ESCI dataset for training"""
    print("Loading ESCI dataset...")
    esci = load_dataset("tasksource/esci")
    
    # Convert to pandas dataframes
    train_df = esci["train"].to_pandas()
    val_df = esci["test"].to_pandas()
    
    # Filter for entries with small_version==1
    train_df = train_df[train_df["small_version"] == 1]
    val_df = val_df[val_df["small_version"] == 1]
    
    print(f"Loaded {len(train_df)} training examples and {len(val_df)} validation examples")
    return train_df, val_df

def main():
    logger = logging.getLogger(__name__)
    
    logger.info("Starting semantic search training with bi-encoder")
    logger.info(f"Configuration: {config}")
    # Load data
    train_df, val_df = load_and_prepare_data()
    
    # Initialize tokenizer
    print(f"Initializing tokenizer: {config['model_name']}")
    tokenizer = AutoTokenizer.from_pretrained(config['model_name'])
    
    # Create datasets
    train_dataset = AmazonESCIDataset(train_df, train_df, tokenizer, config['max_length'])
    val_dataset = AmazonESCIDataset(val_df, val_df, tokenizer, config['max_length'])
    
    # Create dataloaders
    train_loader = DataLoader(train_dataset, batch_size=config['batch_size'], shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=config['batch_size'])
    
    # Initialize model and optimizer
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f"Using device: {device}")
    
    model = BiEncoder(config['model_name']).to(device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=config['learning_rate'])
    criterion = nn.MSELoss()
    
    # Training loop
    print("Starting training...")
    for epoch in range(config['epochs']):
        train_loss = train_epoch(epoch, model, train_loader, optimizer, criterion, device)
        print(f'Epoch {epoch + 1}/{config["epochs"]}, Loss: {train_loss:.4f}')
    
    # Save model
    model_path = 'bi_encoder_model.pth'
    torch.save(model.state_dict(), model_path)
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    main() 