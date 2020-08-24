import smtplib
from email.mime.text import MIMEText
from email_formatter import Email
import os

class Email_Sender:

	def __init__(self):
		self.email = Email()
		self.server = smtplib.SMTP('smtp.gmail.com', 587)
		self.server.ehlo()
		self.server.starttls()
		self.server.ehlo()
		self.server.login(os.getenv('email_from'), os.getenv('emai_password'))

	def send_email(self, item_list):
		email_contents = MIMEText(self.email.get_email(item_list), "html")
		email_contents["From"] = os.getenv('email_from')
		email_contents["To"] = os.getenv('email_to')
		email_contents["Subject"] = "Price Tracker Daily Update"
		self.server.sendmail(os.getenv('email_from'), os.getenv('email_to'), email_contents.as_string())