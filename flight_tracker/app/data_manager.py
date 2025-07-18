import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import json

# Load environment variables from .env file
load_dotenv()

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/5321732fb7ba1620df0f7f5e2896d828/trackerFlightDeals/prices"


class DataManager:

    def __init__(self):
        self.sheety_headers = {
            "Authorization": f"Bearer {os.environ['SHEETY_TOKEN']}"
        }
        self.destination_data = {}

    def get_destination_data(self):
        """
        Get destination data from Sheety API with proper error handling
        """
        try:
            # Include the authorization headers in the request
            response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=self.sheety_headers)

            print(f"Status Code: {response.status_code}")
            print(f"Response Headers: {response.headers}")
            print(f"Raw Response: {response.text}")

            # Check if the request was successful
            if response.status_code != 200:
                print(f"Error: API returned status code {response.status_code}")
                print(f"Response: {response.text}")
                return []

            # Parse JSON response
            data = response.json()
            print(f"Parsed JSON: {json.dumps(data, indent=2)}")

            # Check if 'prices' key exists
            if "prices" not in data:
                print("Available keys in response:", list(data.keys()))
                # Try common alternative key names
                if "price" in data:
                    self.destination_data = data["price"]
                elif "data" in data:
                    self.destination_data = data["data"]
                else:
                    print("No 'prices' key found in response")
                    return []
            else:
                self.destination_data = data["prices"]

            return self.destination_data

        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return []
        except json.JSONDecodeError as e:
            print(f"Failed to parse JSON: {e}")
            print(f"Response text: {response.text}")
            return []
        except KeyError as e:
            print(f"Missing environment variable: {e}")
            return []
        except Exception as e:
            print(f"Unexpected error: {e}")
            return []

    def update_destination_codes(self):
        """
        Update destination codes with proper error handling
        """
        if not self.destination_data:
            print("No destination data to update")
            return

        for city in self.destination_data:
            # Check if city has required fields
            if 'id' not in city:
                print(f"Skipping city {city.get('city', 'Unknown')}: No ID field")
                continue

            if 'iataCode' not in city or not city['iataCode']:
                print(f"Skipping city {city.get('city', 'Unknown')}: No IATA code")
                continue

            # Sheety expects the data wrapped in an object named after your sheet
            # Since your sheet is called "prices", the key should be "price" (singular)
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }

            try:
                # The endpoint format: base_url/[Object ID]
                update_url = f"{SHEETY_PRICES_ENDPOINT}/{city['id']}"
                print(f"Updating {city.get('city', 'Unknown')} at URL: {update_url}")
                print(f"Sending data: {new_data}")

                response = requests.put(
                    url=update_url,
                    json=new_data,
                    headers=self.sheety_headers
                )

                print(f"Update response for {city.get('city', 'Unknown')}: {response.status_code}")

                if response.status_code == 200:
                    print(f"✅ Successfully updated {city.get('city', 'Unknown')} with IATA code: {city['iataCode']}")
                else:
                    print(f"❌ Error updating {city.get('city', 'Unknown')}: {response.status_code}")
                    print(f"Response: {response.text}")

            except Exception as e:
                print(f"❌ Exception updating city {city.get('city', 'Unknown')}: {e}")