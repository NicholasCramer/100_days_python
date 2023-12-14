from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_data_from_sheet()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "DEN"

if sheet_data[0]["iataCode"] == "":
    city_names = [row["city"] for row in sheet_data]
    data_manager.city_codes = flight_search.get_destination_codes(city_names)
    data_manager.update_destination_codes()
    sheet_data = data_manager.get_data_from_sheet()

destinations = {
    data["iataCode"]: {
        "id": data["id"],
        "city": data["city"],
        "price": data["lowestPrice"]
    } for data in sheet_data
}

tomorrow = datetime.now() + timedelta(days=1)
six_month_period = datetime.now() + timedelta(days=(6 * 30))

for destination_code in destinations:
    flight = flight_search.check_flights(
        origin_city_code=ORIGIN_CITY_IATA,
        destination_city_code=destination_code,
        from_time=tomorrow,
        to_time=six_month_period
    )

    if flight is None:
        continue

    if flight.price < destinations[destination_code]["price"]:
        message = (f"Low price alert! Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} \n "
                   f"to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} \n "
                   f"to {flight.return_date}.")

        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

        notification_manager.send_notification(message=message)
