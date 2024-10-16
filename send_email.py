import smtplib
import os
from dotenv import load_dotenv
load_dotenv()

MY_EMAIL = os.environ.get('EMAIL')
PASSWORD = os.environ.get('PASSWORD')
TO_EMAIL = os.environ.get('TO_EMAIL')

class SendEmail:
    def __init__(self, name, email, phone_number, message) -> None:
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.message = message
        self.message_body = f'Subject:New Message from Subscriber: {self.name}\n\nName: {self.name}' \
        f'\nPhone Number: {self.phone_number}' \
        f'\nEmail: {self.email}' \
        f'\nMessage: {self.message}'
        
    def send_email_notification(self):
        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL,
                                    to_addrs=TO_EMAIL,
                                    msg=self.message_body)
        except Exception as e:
            print(f'Unable to send email due to: {e}')