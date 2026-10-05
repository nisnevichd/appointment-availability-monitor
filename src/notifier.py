import os

import requests
from dotenv import load_dotenv

load_dotenv()

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

def send_discord_notification(message):
    if not DISCORD_WEBHOOK_URL:
        raise RuntimeError("DISCORD_WEBHOOK_URL is not configured")

    response = requests.post(
        DISCORD_WEBHOOK_URL,
        json = {'content': message},
        timeout=10
    )

    response.raise_for_status()