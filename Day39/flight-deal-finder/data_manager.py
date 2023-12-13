import requests
from credentials import token

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/e196c54a04da1aa1f67bd51d9830a3d0/flightDeals/prices"
TOKEN = token
AUTH_HEADER = {
    "Authorization": f"Bearer {TOKEN}"
}


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.destination_data = {}

    def get_data_from_sheet(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=AUTH_HEADER)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city["id"]}",
                json=new_data,
                headers=AUTH_HEADER
            )
            print(response.text)
