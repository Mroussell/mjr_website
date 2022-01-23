"""
MJR
Michael Roussell
Copyright 2022

This file handles the email contact functionality.

Python 3.9.7 version of the python interpreter.
If there are any questions, please contact me at 'mjr.dev.contact@gmail.com.

MIT Education License Preferred.
"""
import os
import smtplib
from dotenv import load_dotenv

class ContactHandler:

	def sendContactEmail(self, subject, body):
		# Load environment for email auth.
		load_dotenv()
		email_acc = os.getenv("EMAIL_ACC")
		email_pas = os.getenv("EMAIL_PASS")

		# Set up message information
		sender = email_acc
		to = email_acc
		sub = subject
		bod = body

		email_text = 'Subject: {}\n\n{}'.format(sub, bod)

		try:
			smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
			smtp_server.ehlo()
			smtp_server.login(email_acc, email_pas)
			smtp_server.sendmail(sender, to, email_text)
			smtp_server.close()
			print(f"Email sent to {to} from {email_acc} containing subject: {sub} and body: {bod}." )
		except Exception as ex:
			print(f"Email failed to send with error: {ex}")
