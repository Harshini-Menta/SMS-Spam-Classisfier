# Spam-Classisfier
## Overview:
This repository contains code for a spam detection system. The system analyzes text messages and classifies them as either spam or ham (non-spam). It includes data preprocessing, feature extraction, model training, evaluation, and model saving functionalities.

## Dependencies:
Python 3.x

Libraries: pandas, numpy, scikit-learn, matplotlib, seaborn, nltk, wordcloud, gensim

## Usage:

1. Clone the repository to your local machine.

2. Install the required dependencies using pip:
```
pip install -r requirements.txt
```

3. Ensure that the dataset spam.csv is placed in the src directory.

4. Run the main script 'app.py':
```
python spam_detection.py
```

5. The script will perform the following steps:

-Import the dataset and perform initial data exploration.

-Clean the data by removing unnecessary columns, handling missing values, and eliminating duplicates.

-Analyze the data by visualizing the distribution of spam and ham messages, as well as extracting text statistics.

-Preprocess the text data by removing stopwords, punctuation, and stemming.

-Convert the text data into different representations such as Bag of Words, TF-IDF, and Word2Vec.

-Train various classification models including KNN, Decision Tree, SVM, Naive Bayes, and Random Forest using different text representations.

-Evaluate the models based on accuracy and precision.

-Save the best performing model along with the vectorizer and text preprocessing function using pickle for future use.

