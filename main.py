import smtplib
from email.message import EmailMessage #"""make it easier to build email message"""
import pandas as pd
import schedule
import time
from dotenv import load_dotenv
import os



"""Load your credentials from the .env"""
load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL")
EMAIL_APP_PASSWORD = os.getenv("PASSWORD")


"""send email"""
def send_email(to_address, subject, body):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to_address
    msg.set_content(body)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = EMAIL_ADDRESS, password = EMAIL_APP_PASSWORD)
        connection.send_message(msg)
        print(f"Email sent to the {to_address}")


"""Contact List from the csv"""
def get_contacts(file_path):
    return pd.read_csv(file_path).to_dict(orient = "records")


"""Load email template and customize it"""
def load_template(template_path, name):
    with open(template_path, "r") as template:
        template_content = template.read()
        return template_content.replace("[name]", name)

"""Send emails to everyone"""
def send_to_all():
    contacts = get_contacts("contacts.csv")
    for contact in contacts:
        body = load_template("./templates/welcome_template.txt", contact["name"])
        send_email(contact["email"], "Welcome to Automail", body)


'''Schedule it automatically'''
# schedule.every().day.at("09:00").do(send_to_all)
schedule.every(10).seconds.do(send_to_all)
# comment out this after done checking and use the line above it and arrange it however you wanat.


"""Run forever"""
while True:
    schedule.run_pending()
    time.sleep(1)
