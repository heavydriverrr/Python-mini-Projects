import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

# Configuration constants
WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/forecast"
OPENWEATHER_KEY = os.environ.get("OWM_API_KEY")
TWILIO_SID = "YOUR ACCOUNT SID"
TWILIO_TOKEN = os.environ.get("AUTH_TOKEN")

# Location coordinates and request parameters
request_config = {
    "lat": 76.947975,
    "lon": -7.447447,
    "appid": OPENWEATHER_KEY,
    "cnt": 4,
}


def fetch_weather_forecast():
    """Retrieve weather forecast data from OpenWeatherMap API"""
    api_response = requests.get(WEATHER_API_URL, params=request_config)
    api_response.raise_for_status()
    return api_response.json()


def check_rain_probability(forecast_data):
    """Analyze weather conditions to determine if rain is expected"""
    rain_expected = False

    for weather_entry in forecast_data["list"]:
        weather_id = weather_entry["weather"][0]["id"]
        if int(weather_id) < 700:
            rain_expected = True
            break

    return rain_expected


def send_rain_notification():
    """Send SMS notification about expected rain"""
    http_proxy_client = TwilioHttpClient()
    http_proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    twilio_service = Client(TWILIO_SID, TWILIO_TOKEN, http_client=http_proxy_client)

    notification = twilio_service.messages.create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="YOUR TWILIO VIRTUAL NUMBER",
        to="YOUR TWILIO VERIFIED REAL NUMBER"
    )

    print(notification.status)


# Execute the weather check immediately
forecast_info = fetch_weather_forecast()

if check_rain_probability(forecast_info):
    send_rain_notification()