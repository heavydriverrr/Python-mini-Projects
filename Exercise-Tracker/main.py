import requests
import os
from datetime import datetime
from dotenv import load_dotenv


class ExerciseTracker:
    """Track exercises using Nutritionix API and log to Google Sheets via Sheety."""

    def __init__(self):
        # User profile configuration
        self.user_profile = {
            "gender": "male",
            "weight_kg": 69,
            "height_cm": 185,
            "age": 20
        }

        # API endpoints
        self.nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

        # Load environment variables
        load_dotenv(".env")
        self._setup_credentials()

    def _setup_credentials(self):
        """Load API credentials from environment variables."""
        try:
            self.nutritionix_headers = {
                "x-app-id": os.environ["ENV_NIX_APP_ID"],
                "x-app-key": os.environ["ENV_NIX_API_KEY"]
            }

            self.sheety_endpoint = os.environ["ENV_SHEETY_ENDPOINT"]
            self.sheety_headers = {
                "Authorization": f"Bearer {os.environ['ENV_SHEETY_TOKEN']}"
            }

        except KeyError as e:
            raise EnvironmentError(f"Missing environment variable: {e}")

    def get_exercise_data(self, exercise_text):
        """Fetch exercise data from Nutritionix API."""
        parameters = {
            "query": exercise_text,
            "gender": self.user_profile["gender"],
            "weight_kg": self.user_profile["weight_kg"],
            "height_cm": self.user_profile["height_cm"],
            "age": self.user_profile["age"]
        }

        try:
            response = requests.post(
                self.nutritionix_endpoint,
                json=parameters,
                headers=self.nutritionix_headers
            )
            response.raise_for_status()

            result = response.json()
            print(f"Nutritionix API call: \n {result} \n")
            return result

        except requests.RequestException as e:
            print(f"Error fetching exercise data: {e}")
            return None

    def log_to_sheet(self, result):
        """Log exercise data to Google Sheets via Sheety API."""
        if not result or "exercises" not in result:
            print("No exercise data to log")
            return

        # Adding date and time
        today_date = datetime.now().strftime("%d/%m/%Y")
        now_time = datetime.now().strftime("%X")

        # Sheety Project API
        GOOGLE_SHEET_NAME = "workout"

        for exercise in result["exercises"]:
            sheet_inputs = {
                GOOGLE_SHEET_NAME: {
                    "date": today_date,
                    "time": now_time,
                    "exercise": exercise["name"].title(),
                    "duration": exercise["duration_min"],
                    "calories": exercise["nf_calories"]
                }
            }

            try:
                sheet_response = requests.post(
                    self.sheety_endpoint,
                    json=sheet_inputs,
                    headers=self.sheety_headers
                )
                sheet_response.raise_for_status()
                print(f"Sheety Response: \n {sheet_response.text}")

            except requests.RequestException as e:
                print(f"Error logging exercise {exercise['name']}: {e}")

    def run(self):
        """Main execution flow with continuous loop."""
        print("Exercise Tracker Started!")
        print("Enter 'quit' or 'exit' to stop the program\n")

        try:
            while True:
                exercise_text = input("Tell me which exercises you did: ")

                # Check for exit commands
                if exercise_text.lower().strip() in ['quit', 'exit', 'q']:
                    print("Goodbye! Stay healthy!")
                    break

                if not exercise_text.strip():
                    print("No exercise input provided. Please try again.\n")
                    continue

                # Get exercise data from Nutritionix
                result = self.get_exercise_data(exercise_text)

                # Log to Google Sheets
                self.log_to_sheet(result)

                print("-" * 50)  # Separator for clarity

        except KeyboardInterrupt:
            print("\n\nExecution cancelled by user. Goodbye!")
        except Exception as e:
            print(f"Unexpected error: {e}")


def main():
    """Entry point for the exercise tracking application."""
    tracker = ExerciseTracker()
    tracker.run()


if __name__ == "__main__":
    main()