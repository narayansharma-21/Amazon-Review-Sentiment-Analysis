#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import gzip

from sklearn.metrics import precision_recall_fscore_support, accuracy_score, mean_absolute_error, roc_auc_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from transformers import BertTokenizerFast, BertForSequenceClassification, Trainer, TrainingArguments
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from datasets import Dataset
import torch
import numpy as np
import json

def parse(path):
  g = gzip.open(path, 'rb')
  for l in g:
    yield json.loads(l)

def getDF(path):
  df = {}
  for i, d in enumerate(parse(path)):
    df[i] = d
  return pd.DataFrame.from_dict(df, orient='index')

df = getDF('../../../data/raw/AMAZON_FASHION.json.gz')


# In[8]:


# Drop reviews with no reviewText since we are primarily interested in analyzing review text
df = df.dropna(subset=['reviewText'])

df['overallInt'] = df['overall'].astype(int)
df['reviewText'] = df['reviewText'].astype(str)
df['reviewFull'] = df['reviewText']
df['reviewFull'] = df['reviewFull'].astype(str)
df.head()


# In[9]:


# Keep relevant columns
df = df[['reviewText', 'overall', 'overallInt', 'reviewFull']]
df['overallInt'] = df['overallInt'].apply(lambda x: x - 1)
df['overall'] = df['overall'].apply(lambda x: x - 1)

df.head()


# In[10]:


# Split data into train and test sets
df_train, df_test = train_test_split(df, test_size=0.2, random_state=42)


# In[11]:


train_dataset = Dataset.from_pandas(df_train)
test_dataset = Dataset.from_pandas(df_test)


# In[12]:


tokenizer = AutoTokenizer.from_pretrained('distilbert-base-uncased')

def tokenize(batch):
    tokenized_inputs = tokenizer(batch['reviewText'], padding=True, truncation=True, max_length=128, return_tensors='pt')
    #tokenized_inputs["labels"] = torch.tensor(batch['overall'])
    tokenized_inputs["labels"] = torch.tensor(batch['overallInt'])
    tokenized_inputs['input_ids'] = tokenized_inputs['input_ids'].squeeze(0)
    tokenized_inputs['attention_mask'] = tokenized_inputs['attention_mask'].squeeze(0)

    return tokenized_inputs

train_dataset = Dataset.from_pandas(df_train).map(tokenize, batched=True)
test_dataset = Dataset.from_pandas(df_test).map(tokenize, batched=True)


# In[13]:


train_dataset.set_format('torch', columns=['input_ids', 'attention_mask', 'labels'])
test_dataset.set_format('torch', columns=['input_ids', 'attention_mask', 'labels'])


# In[14]:


# Initializing the model
model = AutoModelForSequenceClassification.from_pretrained(
    'distilbert-base-uncased',
    num_labels=len(np.unique(df['overall']))
)


# In[15]:


# Function to compute metrics
def compute_metrics(pred):
    labels = pred.label_ids
    preds = pred.predictions

    # Hard predictions are needed for accuracy, precision, recall, and F1
    hard_preds = np.argmax(preds, axis=1)

    precision, recall, f1, _ = precision_recall_fscore_support(labels, hard_preds, average='weighted')
    acc = accuracy_score(labels, hard_preds)
    mae = mean_absolute_error(labels, hard_preds)

    # Compute ROC AUC for each class
    roc_auc = {}
    for i in range(preds.shape[1]):  # Iterate over each class
        roc_auc[f"roc_auc_class_{i}"] = roc_auc_score((labels == i).astype(int), preds[:, i])

    return {
        'accuracy': acc,
        'f1': f1,
        'precision': precision,
        'recall': recall,
        'mae': mae,
        **roc_auc  # This will expand the dictionary to include the roc_auc for each class
    }


# In[16]:


training_args = TrainingArguments(
    output_dir='/results',
    num_train_epochs=3,
    per_device_train_batch_size=128,
    per_device_eval_batch_size=128,
    learning_rate=1e-5,
    weight_decay=0.01,
    logging_dir='/logs',
    evaluation_strategy="epoch",
    save_strategy="epoch",
    load_best_model_at_end=True,
    logging_steps=10,
    fp16=True
)


# In[17]:


trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset,
    compute_metrics=compute_metrics,
)


# In[18]:


trainer.train()


# In[ ]:


# Save the model
model.save_pretrained('../../../models/distilbert_amazon_fashion_ver2')


# In[ ]:


# Evaluating the model on the test dataset
trainer.evaluate()
