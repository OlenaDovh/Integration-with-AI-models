import json
import os
from dotenv import load_dotenv
from google.oauth2 import service_account

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
GOOGLE_CLOUD_PROJECT = os.getenv("GOOGLE_CLOUD_PROJECT")
GOOGLE_CLOUD_LOCATION = os.getenv("GOOGLE_CLOUD_LOCATION")
GOOGLE_CREDENTIALS_JSON = os.getenv("GOOGLE_CREDENTIALS_JSON")

credentials = None

if GOOGLE_CREDENTIALS_JSON:
    credentials_info = json.loads(GOOGLE_CREDENTIALS_JSON)
    credentials = service_account.Credentials.from_service_account_info(
        credentials_info,
        scopes=["https://www.googleapis.com/auth/cloud-platform"]
    )