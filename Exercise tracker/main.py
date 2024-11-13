import requests
from datetime import datetime

NUTRITIONIX_API = "https://trackapi.nutritionix.com/v2/natural/exercise"
NUTRITIONIX_API_KEY = "Your API key"
SHEETY_API = "Your Sheety API"
GENDER = "Your gender"
WEIGHT_KG = "Your weight in kilograms"
HEIGHT_CM = "Your height in centimetres"
AGE = "Your age"
API_ID = "Your API ID"
API_KEY = "Your API key"

exercise = {
    "query": input("What sort of exercise(s) did you do and for how long (duration/time)?: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY
}

response = requests.post(url = NUTRITIONIX_API, json = exercise, headers = headers)
data = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(SHEETY_API, json=sheet_inputs)
    print(sheet_response.txt)
