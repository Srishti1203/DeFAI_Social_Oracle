# main.py
from social_monitor import get_tweets, get_reddit_posts, client
from sentiment_analysis import analyze_sentiment
from market_prediction import predict_market
from blockchain_actions import execute_trade
from user_interaction import tweet, send_discord_message

def main():
    # Step 1: Monitor social media
    print("Monitoring social media...")
    tweets = get_tweets("Sonic blockchain")
    reddit_posts = get_reddit_posts("Sonic blockchain")

    # Step 2: Analyze sentiment
    print("Analyzing sentiment...")
    for tweet_text in tweets:
        sentiment, score = analyze_sentiment(tweet_text)
        print(f"Tweet: {tweet_text}\nSentiment: {sentiment}, Score: {score}")

    # Step 3: Predict market
    print("Predicting market...")
    sentiment_scores = [0.8, 0.6, 0.9]  # Example sentiment scores
    historical_prices = [100, 105, 110]  # Example historical prices
    prediction = predict_market(sentiment_scores, historical_prices)
    print(f"Market Prediction: {prediction}")

    # Step 4: Execute on-chain action (example)
    print("Executing on-chain action...")
    execute_trade(10, "SONIC")

    # Step 5: Post insights on Discord/Twitter
    print("Posting insights...")
    tweet("Market prediction: Sonic blockchain is trending positively!")
    send_discord_message('YOUR_CHANNEL_ID', "Market prediction: Sonic blockchain is trending positively!")

if __name__ == "__main__":
    main()