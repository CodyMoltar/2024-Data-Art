# based on https://medium.com/@rslavanyageetha/vader-a-comprehensive-guide-to-sentiment-analysis-in-python-c4f1868b0d2e#:~:text=Vader%20is%20a%20pre%2Dtrained%20model%20that%20uses%20a%20lexicon,overall%20sentiment%20of%20a%20text

# package install:
# pip install nltk

import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer


from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Create an instance of the Vader sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# List of example texts to analyze
texts = [
    "I love this product! It works great and is very affordable.",
    "This product is okay. It gets the job done, but could be better.",
    "I hate this product. It doesn't work at all and is a waste of money."
]

# Loop through the texts and get the sentiment scores for each one
for text in texts:
    scores = analyzer.polarity_scores(text)
    print(text)
    print(scores)