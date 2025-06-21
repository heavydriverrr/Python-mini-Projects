import requests
from dotenv import load_dotenv
from twilio.rest import Client
import os
from twilio.http.http_client import TwilioHttpClient
import dotenv

load_dotenv()

# Twilio configuration
SMS_FROM_NUMBER = "+12184005432"
SMS_TO_NUMBER = "+919625264115"

# Target stock settings
TICKER_SYMBOL = "TSLA"
CORPORATION_NAME = "Tesla Inc"

# API endpoints
MARKET_DATA_URL = "https://www.alphavantage.co/query"
HEADLINES_URL = "https://newsapi.org/v2/everything"

# Authentication keys
MARKET_API_TOKEN = os.environ["MARKET_API_TOKEN"]
HEADLINES_API_TOKEN = os.environ["HEADLINES_API_TOKEN"]
SMS_ACCOUNT_ID = os.environ["Twilio_ID"]
SMS_AUTH_KEY = os.environ["Twilio_key"]

def fetch_stock_data():
    """Retrieve daily stock price data from market API"""
    market_request_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": TICKER_SYMBOL,
        "apikey": MARKET_API_TOKEN,
    }

    api_response = requests.get(MARKET_DATA_URL, params=market_request_params)
    time_series_data = api_response.json()["Time Series (Daily)"]
    return time_series_data


def analyze_price_movement(price_data):
    """Calculate price change percentage between recent trading days"""
    daily_records = [value for (key, value) in price_data.items()]

    # Extract recent closing prices
    latest_session = daily_records[0]
    latest_close = latest_session["4. close"]
    print(latest_close)

    previous_session = daily_records[1]
    previous_close = previous_session["4. close"]
    print(previous_close)

    # Calculate price movement
    price_delta = float(latest_close) - float(previous_close)
    trend_indicator = None
    if price_delta > 0:
        trend_indicator = "🔺"
    else:
        trend_indicator = "🔻"

    # Compute percentage change
    change_percentage = round((price_delta / float(previous_close)) * 100)
    print(change_percentage)

    return change_percentage, trend_indicator


def retrieve_news_articles():
    """Fetch recent news articles about the target company"""
    headlines_params = {
        "apiKey": HEADLINES_API_TOKEN,
        "qInTitle": CORPORATION_NAME,
    }

    headlines_response = requests.get(HEADLINES_URL, params=headlines_params)
    news_items = headlines_response.json()["articles"]

    # Get top 3 articles
    top_stories = news_items[:3]
    print(top_stories)

    return top_stories


def format_alert_messages(articles, percentage, indicator):
    """Create formatted SMS messages for each news article"""
    message_list = [
        f"{TICKER_SYMBOL}: {indicator}{percentage}%\nHeadline: {story['title']}. \nBrief: {story['description']}" for
        story in articles]
    print(message_list)
    return message_list


def send_sms_alerts(formatted_messages):
    """Dispatch SMS notifications via messaging service"""

    messaging_client = Client(SMS_ACCOUNT_ID, SMS_AUTH_KEY,)

    for alert_text in formatted_messages:
        notification = messaging_client.messages.create(
            body=alert_text,
            from_=SMS_FROM_NUMBER,
            to=SMS_TO_NUMBER
        )


# Main execution flow
market_info = fetch_stock_data()
percent_change, movement_symbol = analyze_price_movement(market_info)

# Check if price movement exceeds threshold
if abs(percent_change) > 1:
    latest_news = retrieve_news_articles()
    alert_messages = format_alert_messages(latest_news, percent_change, movement_symbol)
    send_sms_alerts(alert_messages)