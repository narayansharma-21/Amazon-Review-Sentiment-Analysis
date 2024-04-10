# Distilbert for Classification

* Architecture:
  * [distilbert (distilbert-base-uncased)](https://huggingface.co/docs/transformers/en/model_doc/distilbert) Model transformer (with standard Attention. experimented with Flash-atten-2 but final model ended up being with standardized attention)
  * A sequence classification/regression head on top (a linear layer on top of the pooled output) with a classification loss (Cross-Entropy) to output/classify between 5 labels
    * 0: 1 star
    * 1: 2 stars
    * 2: 3 stars
    * 3: 4 stars
    * 4: 5 stars
* Finetuning params:
  * num_train_epochs=3
  * per_device_train_batch_size=128
  * per_device_eval_batch_size=128
  * learning_rate=1e-5
  * weight_decay=0.01
  * evaluation_strategy="epoch"
  * save_strategy="epoch"
  * load_best_model_at_end=True
  * logging_steps=10
  * fp16=True
* Finetuning/training details:
  * Epoch 0.0, Loss: 1.5967, Learning rate: 9.993956973652405e-06
  * Epoch 1.0, Loss: 0.6982, Learning rate: 6.6715010877447425e-06
  * Epoch 2.0, Loss: 0.7048, Learning Rate: 3.3369591491418906e-06
  * Epoch 3.0, Loss: 0.6459, Learning Rate': 8.460236886632826e-09
* Final Evaluation:
  * {'eval_loss': 0.6708220839500427, 'eval_accuracy': 0.7276704007796874, 'eval_f1': 0.7101786236033863, 'eval_precision': 0.7056479785656222, 'eval_recall': 0.7276704007796874, 'eval_mae': 0.3343192751627654, 'eval_roc_auc_class_0': 0.9683087808427645, 'eval_roc_auc_class_1': 0.8971394120665372, 'eval_roc_auc_class_2': 0.8895863111032745, 'eval_roc_auc_class_3': 0.7202337475197294, 'eval_roc_auc_class_4': 0.9350791051800198, 'eval_runtime': 289.2483, 'eval_samples_per_second': 610.137, 'eval_steps_per_second': 4.768, 'epoch': 3.0}
* Best Model:
  * {'train_runtime': 7755.3903, 'train_samples_per_second': 273.07, 'train_steps_per_second': 2.134, 'train_loss': 0.6829385551416214, 'epoch': 3.0}
