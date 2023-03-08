import os
import datetime
import requests

GENDER = "GENDER"
WEIGHT_KG = "WEIGHT"
HEIGHT_CM = "HEIGHT"
AGE = "AGE"

# Constants
APP_ID = "ID"
API_KEY = "KEY"
TOKEN = "TOKEN"

# endpoint
exercise_endpoint = "EXCERCICES ENDPOINT"
sheets_endpoint = "SHEETY ENDPOINT"

exercise_text = input("Enter Your workouts: ")
# parameters
parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}


response = requests.post(url=exercise_endpoint, headers=headers, json=parameters)
result = response.json()

print(result)

# ---------- Sheety ---------- #
headers = {"Authorization": f"Basic {TOKEN}"}
today_date = datetime.datetime.now()
date_format = (today_date.strftime("%x"))

today_time = datetime.datetime.now()
time_format = (today_time.strftime("%X"))[:5]
print(date_format)
print(time_format)

for exercise in result["exercises"]:
    workout_data = {
        "workout": {
            "date": date_format,
            "time": time_format,
            "exercise": exercise["name"].title(),
            "duration": (f"{exercise['duration_min']} min"),
            "calories": (f"{exercise['nf_calories']} kcal"),
        }
    }
    response = requests.post(url=sheets_endpoint, json=workout_data, headers=headers)




print("response.status_code =", response.status_code)
print("response.text =", response.text)