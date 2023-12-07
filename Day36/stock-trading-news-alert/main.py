import requests
from discord import SyncWebhook
from credentials import api_key, news_api_key, webhook_url

STOCK_NAME = "GME"
COMPANY_NAME = "GameStop Corp."

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": api_key
}

# Get stock price data
response = requests.get(url=STOCK_ENDPOINT, params=PARAMS)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]
print(stock_data)
data_list = [value for (key, value) in stock_data.items()]
print(data_list)

# Get yesterday's closing price
yesterday_data = data_list[0]
yesterday_closing = yesterday_data["4. close"]
print(yesterday_closing)

# Get day before yesterday's closing price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing)

# Determine the difference between closing price
close_diff = float(yesterday_closing) - float(day_before_yesterday_closing)
up_down = None
if close_diff > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

# Determine percentage difference
close_diff_percent = round((close_diff / float(yesterday_closing)) * 100)
print(close_diff_percent)

# If difference percentage is greater than 5, get news articles
if abs(close_diff_percent) > 5:
    news_params = {
        "apiKey": news_api_key,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

# Get first three articles from news request
    first_three_articles = articles[:3]
    print(first_three_articles)

# Format the collected articles
    formatted_articles = [f"{STOCK_NAME}:{up_down}{close_diff_percent}%\n"
                          f"Headline:{article['title']}. \nBrief:"
                          f"{article['description']}" for article in first_three_articles]
    print(formatted_articles)

# Send each article to a Discord server using a webhook url
    webhook = SyncWebhook.from_url(webhook_url)
    for article in formatted_articles:
        webhook.send(article)
        print("Message sent to discord.")
