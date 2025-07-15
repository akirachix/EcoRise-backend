import requests
from django.conf import settings
from requests.auth import HTTPBasicAuth
import uuid
import logging

logger = logging.getLogger(__name__)

class DarajaAPI:
    def __init__(self):
        self.consumer_key = settings.DARAJA_CONSUMER_KEY
        self.consumer_secret = settings.DARAJA_CONSUMER_SECRET
        self.business_shortcode = settings.DARAJA_SHORTCODE
        self.base_url = "https://sandbox.safaricom.co.ke"
        self.initiator_name = settings.DARAJA_INITIATOR_NAME
        self.security_credential = settings.DARAJA_SECURITY_CREDENTIAL
        self.b2c_result_url = settings.DARAJA_B2C_RESULT_URL
        self.b2c_queue_timeout_url = settings.DARAJA_B2C_QUEUE_TIMEOUT_URL

    def get_access_token(self):
        url = f"{self.base_url}/oauth/v1/generate?grant_type=client_credentials"
        try:
            response = requests.get(url, auth=HTTPBasicAuth(self.consumer_key, self.consumer_secret))
            response.raise_for_status()
            token_data = response.json()
            logger.debug(f"Access token response: {token_data}")
            return token_data['access_token']
        except requests.exceptions.HTTPError as e:
            logger.error(f"HTTP error getting access token: {e}, Response: {e.response.text if e.response else 'No response'}")
            raise
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to get access token: {str(e)}")
            raise
        except KeyError as e:
            logger.error(f"Invalid response format: {e}, Response: {response.text}")
            raise

    def b2c(self, phone_number, amount, remarks, command_id):
        access_token = self.get_access_token()
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
        payload = {
            "InitiatorName": self.initiator_name,
            "SecurityCredential": self.security_credential,
            "CommandID": command_id,
            "Amount": str(amount),
            "PartyA": self.business_shortcode,
            "PartyB": phone_number,
            "Remarks": remarks,
            "QueueTimeOutURL": self.b2c_queue_timeout_url,
            "ResultURL": self.b2c_result_url,
            "Occasion": "Test",
            "OriginatorConversationID": str(uuid.uuid4())  
           
        }
        url = f"{self.base_url}/mpesa/b2c/v3/paymentrequest"
        try:
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()
            logger.debug(f"B2C response: {response.json()}")
            return response.json()
        except requests.exceptions.HTTPError as e:
            logger.error(f"B2C HTTP error: {e}, Response: {e.response.text if e.response else 'No response'}")
            return {"ResponseCode": "1", "ResponseDesc": str(e), "ErrorDetails": e.response.text if e.response else "No response"}
        except requests.exceptions.RequestException as e:
            logger.error(f"B2C failed: {str(e)}")
            return {"ResponseCode": "1", "ResponseDesc": str(e)}