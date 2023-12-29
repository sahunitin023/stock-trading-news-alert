from twilio.rest import Client

account_sid = "TWILIO_ACC_SID"
auth_token = "AUTH_TOKEN"
twilio_number = "Twilio_Number"


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
