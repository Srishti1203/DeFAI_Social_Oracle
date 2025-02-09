# sentiment_analysis.py
from transformers import pipeline

# Initialize sentiment analyzer
sentiment_analyzer = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    result = sentiment_analyzer(text)
    return result[0]['label'], result[0]['score']