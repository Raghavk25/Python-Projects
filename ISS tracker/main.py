# ISS tracker

# MIT License
# Copyright (c) 2024 Raghav Khanna
# See the LICENSE file in the root of the repository for full license details.

import requests
import datetime
import smtplib
import time

MY_EMAIL = "user@gmail.com"
MY_PASSWORD = "password"

MY_LATITUDE = 28.6139
MY_LONGITUDE = 77.2088
# New Delhi's coordinates

def is_close():
    response = requests.get(url = "http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    latitude = float(response.json()["iss_position"]["latitude"])
    longitude = float(response.json()["iss_position"]["longitude"])

    if (MY_LATITUDE - 5 <= latitude <= MY_LATITUDE + 5) and (MY_LONGITUDE - 5 <= longitude <= MY_LONGITUDE + 5):
        return True

def is_night():
    parameters = {
        "lat": MY_LATITUDE,
        "lng": MY_LONGITUDE,
        "time_format": 24,
    }
    response = requests.get(url = "https://api.sunrisesunset.io/json", params = parameters)
    response.raise_for_status()

    sunrise = int(response.json()["results"]["sunrise"].split(":")[0])
    sunset = int(response.json()["results"]["sunset"].split(":")[0])

    time_now = datetime.datetime.now().hour
    
    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_close() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port = 587) as connection:
            connection.starttls()
            connection.login(user = MY_EMAIL, password = MY_PASSWORD)
            connection.sendmail(
                to_addrs = MY_EMAIL,
                from_addr = MY_EMAIL,
                msg = "Subject: Look up!\n\nLook up. The ISS tracker is overhead."
            )
        print(f"\nIt was overhead at {datetime.datetime.now()}.")














