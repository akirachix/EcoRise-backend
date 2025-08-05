
import africastalking
from django.conf import settings
import logging

logger = logging.getLogger('payment')

class SMSNotifier:
    def __init__(self):
        africastalking.initialize(
            username=settings.AFRICASTALKING_USERNAME,
            api_key=settings.AFRICASTALKING_API_KEY
        )
        self.sms = africastalking.SMS

    def notify_receiver(self, receiver_phone: str, amount: str, account_reference: str, status: str):
        message = f"Payment of {amount} KSH for pickup {account_reference} {status}."
        logger.info(f"Preparing to send SMS to {receiver_phone}: {message}")
        try:

            if receiver_phone.startswith('0'):
                receiver_phone = '+254' + receiver_phone[1:]
            elif not receiver_phone.startswith('+254'):
                receiver_phone = '+254' + receiver_phone[3:] if receiver_phone.startswith('254') else receiver_phone
            response = self.sms.send(message, [receiver_phone])
            logger.info(f"SMS sent to {receiver_phone}: {response}")
            return response
        except Exception as e:
            logger.error(f"Failed to send SMS to {receiver_phone}: {str(e)}")
            raise Exception(f"Failed to send SMS: {str(e)}")