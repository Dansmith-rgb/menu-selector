import smtplib, ssl
import m_selector 
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv
import os

load_dotenv(".env")

SENDER = os.environ.get("GMAIL_USER")
PASSWORD = os.environ.get("GMAIL_PASSWORD")
RECIEVER = os.environ.get("GMAIL_RECIEVER")
print(SENDER)
print(PASSWORD)

message = MIMEMultipart()
filename = "Meal_selection.pdf"

part = MIMEBase('application', "octet-stream")
part.set_payload(open("Menu_selection.pdf", "rb").read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

message.attach(part)

s = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465)
s.login(SENDER, PASSWORD)
s.sendmail(SENDER, RECIEVER, message.as_string())
