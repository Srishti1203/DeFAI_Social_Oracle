# social_monitor.py
import tweepy
import praw
import discord
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Twitter API setup
def get_tweets(query, count=10):
    auth = tweepy.OAuth1UserHandler(
        os.getenv("TWITTER_API_KEY"),
        os.getenv("TWITTER_API_SECRET_KEY"),
        os.getenv("TWITTER_ACCESS_TOKEN"),
        os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
    )
    api = tweepy.API(auth)
    tweets = api.search_tweets(q=query, count=count)
    return [tweet.text for tweet in tweets]

# Reddit API setup
def get_reddit_posts(query, limit=10):
    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT")
    )
    posts = reddit.subreddit("all").search(query, limit=limit)
    return [post.title for post in posts]

# Discord bot setup
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    print(f"Message: {message.content}")