import datetime as dt
import random
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

TEST_EMAIL = os.getenv("MY_EMAIL")
APP_PASSWORD = os.getenv("PASSWORD")

# Read the file and extract quotes into a list
with open("quotes.txt") as quotes:
    data = quotes.readlines()

# Pick a random quote from the list
random_quote = random.choice(data).strip().encode('ascii','ignore')
random_quote = random_quote.decode("utf-8","ignore")
print(random_quote)

# Obtain the current day of the week (Wednesday)
day_of_week = dt.datetime.now().weekday()
print(day_of_week)

if dt.datetime.now().weekday() == day_of_week:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=TEST_EMAIL, password=APP_PASSWORD)
        connection.sendmail(
            from_addr=TEST_EMAIL,
            to_addrs=TEST_EMAIL,
            msg=f"Subject:Quote of the day\n\n{random_quote}"
        )