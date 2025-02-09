# user_interaction.py
import tweepy
import discord
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Twitter API setup
def tweet(message):
    auth = tweepy.OAuth1UserHandler(
        os.getenv("TWITTER_API_KEY"),
        os.getenv("TWITTER_API_SECRET_KEY"),
        os.getenv("TWITTER_ACCESS_TOKEN"),
        os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
    )
    api = tweepy.API(auth)
    api.update_status(message)

# Discord bot setup
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

async def send_discord_message(channel_id, message):
    channel = client.get_channel(channel_id)
    await channel.send(message)