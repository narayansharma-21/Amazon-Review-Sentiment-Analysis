# Distilbert for Classification

* Architecture:
  * [distilbert (distilbert-base-uncased)](https://huggingface.co/docs/transformers/en/model_doc/distilbert) Model transformer (tested with Flash and standard Attention)
  * A sequence classification/regression head on top (a linear layer on top of the pooled output) with a classification loss (Cross-Entropy) to output/classify between 5 labels
    * 0: 1 star
    * 1: 2 stars
    * 2: 3 stars
    * 3: 4 stars
    * 4: 5 stars
* 
