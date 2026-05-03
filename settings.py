from dotenv import load_dotenv
import json
import os
from google.oauth2 import service_account

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
GOOGLE_CLOUD_PROJECT = os.getenv("GOOGLE_CLOUD_PROJECT")
GOOGLE_CLOUD_LOCATION = os.getenv("GOOGLE_CLOUD_LOCATION")

credentials_json = os.getenv("GOOGLE_CREDENTIALS_JSON")

if credentials_json:
    credentials_dict = json.loads(credentials_json)
    credentials = service_account.Credentials.from_service_account_info(credentials_dict)
else:
    credentials = None