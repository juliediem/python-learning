##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import smtplib
import datetime as dt
import random
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

TEST_EMAIL = os.getenv("MY_EMAIL")
APP_PASSWORD = os.getenv("PASSWORD")

#Open csv data
df = pd.read_csv("birthdays.csv")

# Find current date
current_month = dt.datetime.now().month
current_day = dt.datetime.now().day


# Create definition to pick a random letter template
def pick_letter_template():
    all_letter_templates = os.listdir("letter_templates")
    letter_template = random.choice(all_letter_templates)
    with open(f"letter_templates/{letter_template}") as file:
        final_letter = file.read()
    return final_letter


# Create definition to replace [NAME] with name of person
def mail_merge(letter_template, name):
    output_letter = letter_template.replace("[NAME]", name.strip())
    return output_letter

    # Create definition to send email


def send_email(email, password, provider, message):
    with smtplib.SMTP(provider) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=email,
            msg=f"Subject:Happy Birthday\n\n{message}"
        )


for index, row in df.iterrows():
    if (row["month"] == current_month) & (row["day"] == current_day):
        print(row["name"])
        letter = mail_merge(pick_letter_template(), row['name'])
        print(letter)
        send_email(email=TEST_EMAIL, password=APP_PASSWORD, provider="smtp.gmail.com", message=letter)

# Find all potential letter templates and put them in a list
