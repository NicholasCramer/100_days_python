import requests
from datetime import datetime
from credentials import app_id, api_key, token

APP_ID = app_id
API_KEY = api_key
TOKEN = token

GENDER = "male"
WEIGHT_KG = "72.5"
HEIGHT_CM = "183"
AGE = "29"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

parameters = {
    "query": "Walked for 1 hour",
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()

today = datetime.now().strftime("%m/%d/%Y")
time = datetime.now().strftime("%H:%M:%S")

# Sheety api. Used to update google sheet
sheety_endpoint = "https://api.sheety.co/e196c54a04da1aa1f67bd51d9830a3d0/workoutTracking/workouts"

auth_header = {
    "Authorization": f"Bearer {TOKEN}"
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    post_response = requests.post(url=sheety_endpoint, json=sheet_inputs, headers=auth_header)
    print(post_response.text)
