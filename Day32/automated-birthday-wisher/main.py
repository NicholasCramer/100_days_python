from credentials import username, password
from datetime import datetime
import smtplib
import pandas
import random

today = (datetime.now().month, datetime.now().day)

data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_template:
        letter_data = letter_template.read()\

    new_contents = letter_data.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("outlook.office365.com") as connection:
        connection.starttls()
        connection.login(user=username, password=password)
        connection.sendmail(
            from_addr=username,
            to_addrs="nick_cramer@outlook.com",
            msg=f"Subject: Happy Birthday!\n\n{new_contents}"
        )
