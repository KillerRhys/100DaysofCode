from twilio.rest import Client
import os

TWILIO_SID = os.environ.get("Twilio_SID")
TWILIO_AUTH_TOKEN = os.environ.get("Twilio_Auth_Token")
TWILIO_VIRTUAL_NUMBER = os.environ.get("Twilio_Vir_Num")
TWILIO_VERIFIED_NUMBER = os.environ.get("Twilio_Ver_Num")


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
