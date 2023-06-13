import os
from dotenv import load_dotenv

load_dotenv()

FRESHDESK_DOMAIN = os.getenv('FRESHDESK_DOMAIN', '')

FRESHDESK_URL_ADD_CONTACT = "contacts"
FRESHDESK_ACCOUNT = "account"
GITHUB_URL = "https://api.github.com/user"
FRESHDESK_URL = f"https://{FRESHDESK_DOMAIN}.freshdesk.com/api/v2/"
