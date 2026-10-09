import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("PINTEREST_SANDBOX_ACCESS_TOKEN")

if not TOKEN:
    raise ValueError(
        "PINTEREST_SANDBOX_ACCESS_TOKEN is missing from .env"
    )

BASE_URL = "https://api-sandbox.pinterest.com/v5"

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
}

payload = {
    "name": "Pinterest AI Test",
    "description": "Sandbox board for Pinterest AI Growth Engine testing.",
    "privacy": "PUBLIC",
}

response = requests.post(
    f"{BASE_URL}/boards",
    headers=headers,
    json=payload,
    timeout=30,
)

print("STATUS:", response.status_code)
print("RESPONSE:", response.text)

response.raise_for_status()