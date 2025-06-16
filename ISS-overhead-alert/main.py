import requests
from datetime import datetime
import smtplib
import time

# Configuration constants
USER_EMAIL = ""
USER_PASSWORD = ""
OBSERVER_LAT = 72.507351  # Observer's latitude
OBSERVER_LON = -7.127758  # Observer's longitude

# API endpoints
ISS_POSITION_API = "http://api.open-notify.org/iss-now.json"
SUNRISE_SUNSET_API = "https://api.sunrise-sunset.org/json"


def get_station_coordinates():
    """Fetch current ISS position coordinates"""
    api_response = requests.get(url=ISS_POSITION_API)
    api_response.raise_for_status()
    position_data = api_response.json()

    station_lat = float(position_data["iss_position"]["latitude"])
    station_lon = float(position_data["iss_position"]["longitude"])

    return station_lat, station_lon


def check_station_visibility():
    """Determine if ISS is visible from observer's location"""
    station_lat, station_lon = get_station_coordinates()

    # Check if position is within ±5 degrees of observer location
    lat_in_range = OBSERVER_LAT - 5 <= station_lat <= OBSERVER_LAT + 5
    lon_in_range = OBSERVER_LON - 5 <= station_lon <= OBSERVER_LON + 5

    if lat_in_range and lon_in_range:
        return True
    return False


def check_darkness_conditions():
    """Verify if current time is during night hours"""
    sun_data_params = {
        "lat": OBSERVER_LAT,
        "lng": OBSERVER_LON,
        "formatted": 0,
    }

    sun_response = requests.get(SUNRISE_SUNSET_API, params=sun_data_params)
    sun_response.raise_for_status()
    sun_info = sun_response.json()

    dawn_hour = int(sun_info["results"]["sunrise"].split("T")[1].split(":")[0])
    dusk_hour = int(sun_info["results"]["sunset"].split("T")[1].split(":")[0])

    current_hour = datetime.now().hour

    if current_hour >= dusk_hour or current_hour <= dawn_hour:
        return True
    return False


def dispatch_notification():
    """Send email notification about ISS visibility"""
    email_client = smtplib.SMTP("smtp.google.com")
    email_client.starttls()
    email_client.login(USER_EMAIL, USER_PASSWORD)
    email_client.sendmail(
        from_addr=USER_EMAIL,
        to_addrs=USER_EMAIL,
        msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
    )


# Main monitoring loop
while True:
    time.sleep(60)
    if check_station_visibility() and check_darkness_conditions():
        dispatch_notification()