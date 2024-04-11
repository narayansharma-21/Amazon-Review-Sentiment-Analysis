# Logistic Regression 

## Doc2Vec (w/ reviewText tokens)

### Logistic Regression
              precision    recall  f1-score   support

         1.0       0.52      0.49      0.50     20917
         2.0       0.25      0.01      0.02     12765
         3.0       0.37      0.21      0.27     19019
         4.0       0.41      0.19      0.26     28682
         5.0       0.65      0.93      0.77     88965
    accuracy                           0.60    170348
    macro avg      0.44      0.37      0.36    170348
    weighted avg   0.53      0.60      0.54    170348


### Logistic Regression - (w/ Class Weighting)

Accuracy: 0.5918061849860285


### Logistic Regression - (w/ undersampling majority class)

              precision    recall  f1-score   support

         1.0       0.50      0.58      0.54     20917
         2.0       0.27      0.30      0.29     12765
         3.0       0.36      0.37      0.37     19019
         4.0       0.40      0.49      0.44     28682
         5.0       0.82      0.72      0.77     88965
    accuracy                           0.59    170348
    macro avg      0.47      0.49      0.48    170348
    weighted avg   0.62      0.59      0.60    170348

* Note: Oversampling minority classes produced the same results

### Logistic Regression - (w/ SMOTE technique)

            precision    recall  f1-score   support

         1.0       0.49      0.59      0.53     20917
         2.0       0.28      0.31      0.29     12765
         3.0       0.37      0.38      0.37     19019
         4.0       0.41      0.49      0.45     28682
         5.0       0.83      0.71      0.77     88965
    accuracy                           0.59    170348
    macro avg      0.47      0.50      0.48    170348
    weighted avg   0.62      0.59      0.60    170348


## TFIDF (w/ Summary and reviewText tokens)


### Logistic Regression 

              precision    recall  f1-score   support

         1.0       0.47      0.58      0.52     20917
         2.0       0.27      0.01      0.03     12765
         3.0       0.32      0.14      0.19     19019
         4.0       0.43      0.16      0.23     28682
         5.0       0.66      0.93      0.77     88965
    accuracy                           0.60    170348
    macro avg      0.43      0.36      0.35    170348
    weighted avg   0.53      0.60      0.53    170348

### Logistic Regression - (w/ Class Weighting)

Accuracy: 0.5025946885199709

### Logistic Regression - (w/ undersampling majority class)

              precision    recall  f1-score   support

         1.0       0.37      0.67      0.48     20917
         2.0       0.20      0.25      0.22     12765
         3.0       0.26      0.26      0.26     19019
         4.0       0.32      0.37      0.34     28682
         5.0       0.82      0.59      0.69     88965
    accuracy                           0.50    170348
    macro avg      0.39      0.43      0.40    170348
    weighted avg   0.57      0.50      0.52    170348


* Note: Oversampling minority classes produced the same results


### Logistic Regression - (w/ SMOTE Technique)

              precision    recall  f1-score   support

         1.0       0.49      0.59      0.53     20917
         2.0       0.28      0.31      0.29     12765
         3.0       0.37      0.38      0.37     19019
         4.0       0.41      0.49      0.45     28682
         5.0       0.83      0.71      0.77     88965
    accuracy                           0.59    170348
    macro avg      0.47      0.50      0.48    170348
    weighted avg   0.62      0.59      0.60    170348

