import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

TEST_EMAIL = os.getenv("MY_EMAIL")
APP_PASSWORD = os.getenv("PASSWORD")

# #Manually closing the connection
# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=TEST_EMAIL, password=APP_PASSWORD)
# connection.sendmail(from_addr=TEST_EMAIL, to_addrs=TEST_EMAIL, msg="Subject:Hello\n\nThis is the email body")
# connection.close()

# #Automatically closes connection
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=TEST_EMAIL, password=APP_PASSWORD)
#     connection.sendmail(
#         from_addr=TEST_EMAIL,
#         to_addrs=TEST_EMAIL,
#         msg="Subject:Hi There\n\nThis is an automated message."
#     )


import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(now)
print(day_of_week)

date_of_birth = dt.datetime(year=1994, month=7, day=7)
print(date_of_birth)