from credentials import username, password
import datetime as dt
import smtplib
import random

with open("quotes.txt", mode="r") as motivational_quotes:
    data = motivational_quotes.readlines()

random_quote = random.choice(data)

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 5:
    with smtplib.SMTP("outlook.office365.com") as connection:
        connection.starttls()
        connection.login(user=username, password=password)
        connection.sendmail(from_addr=username, to_addrs="nick_cramer@outlook.com",
                            msg=f"Subject: Motivational Quote\n\n{random_quote}")

