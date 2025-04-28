# market_prediction
from sklearn.linear_model import LinearRegression
import pandas as pd

def predict_market(sentiment_scores, historical_prices):
    model = LinearRegression()
    model.fit(sentiment_scores, historical_prices)
    prediction = model.predict(sentiment_scores[-1].reshape(1, -1))
    return prediction
