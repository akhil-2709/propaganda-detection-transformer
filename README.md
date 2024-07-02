# Detection of Propaganda and Persuasive Texts in Images

## Introduction
This project focuses on identifying and classifying propaganda and persuasive techniques in memes and other text-based images. Memes have become a prevalent medium for communication and information sharing on the internet, often used to influence public opinion subtly.

## Problem Statement
The goal is to develop models that can perform multi-label classification to detect various propaganda techniques within text extracted from images.

## Data and Preprocessing
### Datasets Used
1. **PTC Meme Dataset**: Primary dataset containing memes with labeled persuasion techniques.
2. **PTC News Dataset**: Supplementary dataset with news articles labeled for propaganda techniques.
3. **Generic Meme Dataset**: Used for additional training to enhance model performance.

### Data Preprocessing
- **Tokenization**: Different tokenizers for LSTM, BERT, and T5 models to format the input data appropriately.
- **Data Cleaning**: Standard techniques to ensure data quality.

## Baseline Model
- **Logistic Regression**: Achieved a micro F1 score of 0.07, serving as the baseline for comparison.

## Model Approaches
### LSTM
- Fine-tuned for multi-label classification.
  
### BERT
- Fine-tuned for multi-label classification on various datasets combinations.
  
### T5
- Fine-tuned for generative tasks, adapted for multi-label classification.
- Implemented multi-task training using different prefixes to handle multiple related tasks.

## Implementation
### Subtask 1: Persuasion Technique Classification
- Utilized a combination of datasets to improve model performance.
- Created a two-model pipeline for binary and multi-label classification.

### Subtask 2: Identifying Spans for Each Technique
- Employed T5 model to predict the start and end indices of persuasive techniques in text.

## Results
- **BERT** outperformed other models with a micro F1 score of 0.34 when fine-tuned on a combination of PTC Meme and PTC News datasets.
- **T5** performed well in binary classification but struggled with the complexity of predicting all 20 labels correctly.
