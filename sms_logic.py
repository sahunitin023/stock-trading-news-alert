from twilio.rest import Client

account_sid = 'ACa228bf51b57793614a2a678d22fd88da'
auth_token = '654b2856ae916b3bff91cc6f0dff29f5'
twilio_number = '+17346723505'


class SMSLogic:

    def __init__(self):
        self._client = Client(account_sid, auth_token)

    def send_message(self, message, receiverNumber):

        message_response = self._client.messages.create(
            from_=twilio_number,
            body=message,
            to=receiverNumber
        )

        return message_response
