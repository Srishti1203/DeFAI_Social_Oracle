DeFAI Social Oracle 🚀
An **AI-powered agent** that monitors social media, analyzes sentiment, predicts market trends, and interacts with the **Sonic blockchain**. Built as an **MVP (Minimum Viable Product)** for the **Build the Future of DeFAI Hackathon** by **Sonic** and **DoraHacks**.
## 🌟 Features

- **Social Media Monitoring**: Tracks discussions about Sonic blockchain on Twitter, Reddit, and Discord.
- **Sentiment Analysis**: Uses Hugging Face's AI models to analyze social media sentiment.
- **Market Prediction**: Predicts market trends based on historical data and sentiment analysis.
- **On-Chain Actions**: Executes trades and interacts with the Sonic blockchain.
- **User Interaction**: Posts insights and predictions on Discord and Twitter.
  
## 🛠️ Tech Stack

- **Programming Language**: Python
- **Blockchain Interaction**: Sonic SDK, Web3.py
- **AI/ML**: Hugging Face Transformers, Scikit-learn
- **Social Media APIs**: Twitter API, Reddit API, Discord API
- **Hosting**: PythonAnywhere, Heroku (Free Tier)

---
🏆 Hackathon Submission
This project is an MVP (Minimum Viable Product) built for the Build the Future of DeFAI Hackathon organized by Sonic and DoraHacks. Below are the key details:

Judging Criteria:

Technological Implementation: Demonstrates quality software development and integration with Sonic.

Design: Intuitive user experience and thoughtful design.

Potential Impact: High potential to influence the blockchain industry.

Quality of the Idea: Creative and unique project concept.

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- API keys for Twitter, Reddit, Discord, and OpenAI (if using)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/DeFAI_Social_Oracle.git
   cd DeFAI_Social_Oracle
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add your API keys and tokens:
   ```env
   TWITTER_API_KEY=your_twitter_api_key
   TWITTER_API_SECRET_KEY=your_twitter_api_secret_key
   TWITTER_ACCESS_TOKEN=your_twitter_access_token
   TWITTER_ACCESS_TOKEN_SECRET=your_twitter_access_token_secret

   REDDIT_CLIENT_ID=your_reddit_client_id
   REDDIT_CLIENT_SECRET=your_reddit_client_secret
   REDDIT_USER_AGENT=your_reddit_user_agent

   DISCORD_BOT_TOKEN=your_discord_bot_token
   OPENAI_API_KEY=your_openai_api_key
   ```

## 🧠 How It Works

1. **Social Media Monitoring**: The agent scrapes data from Twitter, Reddit, and Discord for discussions about Sonic blockchain.
2. **Sentiment Analysis**: It uses Hugging Face's AI models to analyze the sentiment of the collected data.
3. **Market Prediction**: Based on historical data and sentiment analysis, the agent predicts market trends.
4. **On-Chain Actions**: The agent executes trades or other actions on the Sonic blockchain.
5. **User Interaction**: Insights and predictions are posted on Discord and Twitter for users to follow.

---

## 📂 Project Structure

```
DeFAI_Social_Oracle/
├── main.py                # Main script to run the agent
├── social_monitor.py      # Social media monitoring
├── sentiment_analysis.py  # Sentiment analysis using AI
├── market_prediction.py   # Market trend prediction
├── blockchain_actions.py  # On-chain actions
├── user_interaction.py    # Posting insights on Discord/Twitter
├── requirements.txt       # List of dependencies
├── .env                   # Environment variables (API keys)
├── README.md              # Project documentation
```
⚠️ Important Note
This project is an MVP and requires users to provide their own API keys and tokens for the following services:

Twitter API

Reddit API

Discord Bot Token

OpenAI API (optional, for advanced features)

These keys and tokens should be added to the .env file as described in the Installation section.

## 🤝 Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request.

---

## 🙏 Acknowledgments

- **Sonic Labs** for organizing the hackathon.
- **Hugging Face** for providing open-source AI models.
- **Twitter**, **Reddit**, and **Discord** for their APIs.
- **Python Community** for amazing libraries and tools.
 📧 Contact

If you have any questions or feedback, feel free to reach out:
Srishti Pandey :pandey.srishti03@gmail.com


