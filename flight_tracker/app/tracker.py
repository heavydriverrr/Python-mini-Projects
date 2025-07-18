from datetime import datetime, timedelta
import time
from app.data_manager import DataManager
from app.flight_search import FlightSearch
from app.flight_data import find_cheapest_flight
from app.notification_manager import NotificationManager

def run_tracker():
    data_manager = DataManager()
    flight_search = FlightSearch()
    notification_manager = NotificationManager()

    sheet_data = data_manager.get_destination_data()

    ORIGIN_CITY_IATA = "DEL"

    for row in sheet_data:
        if row["iataCode"] == "":
            row["iataCode"] = flight_search.get_destination_code(row["city"])
            time.sleep(2)

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

    tomorrow = datetime.now() + timedelta(days=1)
    six_month_from_today = datetime.now() + timedelta(days=180)

    for destination in sheet_data:
        flights = flight_search.check_flights(
            ORIGIN_CITY_IATA,
            destination["iataCode"],
            from_time=tomorrow,
            to_time=six_month_from_today
        )
        cheapest_flight = find_cheapest_flight(flights)
        print(f"Cheapest flight found: ₹{cheapest_flight.price} → {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}")
        print(f"Comparing ₹{cheapest_flight.price} < ₹{destination['lowestPrice']} for {destination['city']}")

        if cheapest_flight.price != "N/A" and float(cheapest_flight.price) < float(destination["lowestPrice"]):
            message = (
                f"Low price alert! Only ₹{cheapest_flight.price} to fly "
                f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                f"from {cheapest_flight.out_date} to {cheapest_flight.return_date}."
            )
            notification_manager.send_whatsapp(message)
