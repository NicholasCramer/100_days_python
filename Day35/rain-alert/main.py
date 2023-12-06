from credentials import api_key, account_sid, auth_token, phone_number
import requests
from twilio.rest import Client

MY_LAT = 45.512230
MY_LON = -122.658722

PARAMS = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": api_key,
    "cnt": 4,
}

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

response = requests.get(url=OWM_Endpoint, params=PARAMS)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☂️",
        from_="+18669682936",
        to=phone_number
    )
    print(message.status)
