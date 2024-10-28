# based on https://medium.com/@rslavanyageetha/vader-a-comprehensive-guide-to-sentiment-analysis-in-python-c4f1868b0d2e#:~:text=Vader%20is%20a%20pre%2Dtrained%20model%20that%20uses%20a%20lexicon,overall%20sentiment%20of%20a%20text

# package install:
# pip install nltk

import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

import os

# Create an instance of the Vader sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

FOLDER = '../data/new-media-student-diary/'

# loop through all the .txt files in the FOLDER
texts = []
for file in os.listdir(FOLDER):
    if file.endswith('.txt'):
        with open(FOLDER + file, 'r') as f:
            # print(file)

            # read the file
            text = f.read()
            scores = analyzer.polarity_scores(text)
            # print(text)
            print(scores)


# Loop through the texts and get the sentiment scores for each one
# for text in texts:
#     scores = analyzer.polarity_scores(text)
#     print(text)
#     print(scores)