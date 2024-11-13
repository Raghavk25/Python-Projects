# Automated Birthday Wisher

# MIT License
# Copyright (c) 2024 Raghav Khanna
# See the LICENSE file in the root of the repository for full license details.

import smtplib
import datetime as dt
import random
import pandas

SENDER_EMAIL = "sender_email@gmail.com"
SENDER_PASSWORD = "sender_password"
# Fill in the sender's email ID and app password (you will have to create an app password in gmail, copy it, and paste it here.)

birthday_data = pandas.read_csv("./birthdays.csv")
birthday_dict = {(row["month"], row["day"]): row["name"] for (index, row) in birthday_data.iterrows()}
birthday_dict_2 = {row["name"]: row["email"] for (index, row) in birthday_data.iterrows()}

today_tuple = (dt.datetime.now().month, dt.datetime.now().day)

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    birthday_person_email = birthday_dict_2[birthday_person]

    with open(f"./letter_format_{random.randint(1, 5)}.txt") as letter_file:
        letter_content = letter_file.read().replace("<NAME>", birthday_person)

    with smtplib.SMTP("smtp.gmail.com", port = 587) as connection:
        # We used port 587 instead of the default port 25 because our ISP, among many other ISPs, blocks the latter.
        connection.starttls()
        connection.login(user = SENDER_EMAIL, password = SENDER_PASSWORD)
        connection.sendmail(
            to_addrs = birthday_person_email,
            from_addr = SENDER_EMAIL,
            msg = f"Subject: Happy Birthday!\n\n{letter_content}"
        )

# This code is not actually automated. You will have to run this every day for it to be effective.
# Alternatively, you can upload it on "PythonAnywhere" cloud where you can set it to run daily automatically. 
