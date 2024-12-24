#Rain alert

import requests
import smtplib

MY_LATITUDE = 28.6139
MY_LONGITUDE = 77.2088
# New Delhi's coordinates

API_KEY = "Your openweathermap.org's API key"
MY_EMAIL = "user@gmail.com"
MY_PASSWORD = "password"

response = requests.get(url = f"https://api.openweathermap.org/data/2.5/forecast?lat={MY_LATITUDE}&lon={MY_LONGITUDE}&appid={API_KEY}&cnt=4")
response.raise_for_status()

will_rain = False
for i in response.json()["list"]:
    if int(i["weather"][0]["id"]) < 700:
        will_rain = True
        
if will_rain:
    print("Carry an umbrella!")
    with smtplib.SMTP("smtp.gmail.com", port = 587) as connection:
        connection.starttls()
        connection.login(user = MY_EMAIL, password = MY_PASSWORD)
        connection.sendmail(
            to_addrs = MY_EMAIL,
            from_addr = MY_EMAIL,
            msg = "Subject: Rain\n\nIt's going to rain today. Carry an umbrella!"
        )

