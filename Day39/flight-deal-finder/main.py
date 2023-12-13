from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_data_from_sheet()
flight_search = FlightSearch()
notification_manager = NotificationManager()
print(sheet_data)

ORIGIN_CITY_IATA = "DEN"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_period = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        origin_city_code=ORIGIN_CITY_IATA,
        destination_city_code=destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_period
    )

    if flight.price < destination["lowestPrice"]:
        notification_manager.send_notification(
            message=f"Low price alert! Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} \n"
                    f"to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} \n"
                    f"to {flight.return_date}."
        )
