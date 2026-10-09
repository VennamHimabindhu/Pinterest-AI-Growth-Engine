import os
import secrets
from urllib.parse import urlencode

import requests
from dotenv import load_dotenv


# Load values from .env
load_dotenv()


class PinterestAuth:

    AUTH_URL = "https://www.pinterest.com/oauth/"
    TOKEN_URL = "https://api.pinterest.com/v5/oauth/token"

    def __init__(self):
        self.client_id = os.getenv("PINTEREST_CLIENT_ID")
        self.client_secret = os.getenv("PINTEREST_CLIENT_SECRET")
        self.redirect_uri = os.getenv(
            "PINTEREST_REDIRECT_URI",
            "http://localhost:8000/callback"
        )

    # -------------------------------------------------
    # 1. Create Pinterest authorization URL
    # -------------------------------------------------

    def get_authorization_url(self):

        # Helps protect the OAuth flow
        state = secrets.token_urlsafe(16)

        params = {
    "client_id": self.client_id,
    "redirect_uri": self.redirect_uri,
    "response_type": "code",

    "scope": (
        "boards:read,"
        "boards:write,"
        "pins:read,"
        "pins:write,"
        "user_accounts:read"
    ),

    "state": state
}

        authorization_url = (
            f"{self.AUTH_URL}?{urlencode(params)}"
        )

        return authorization_url, state


    # -------------------------------------------------
    # 2. Exchange authorization code for access token
    # -------------------------------------------------

    def exchange_code_for_token(self, code):

        response = requests.post(
            self.TOKEN_URL,

            # HTTP Basic Authentication
            auth=(
                self.client_id,
                self.client_secret
            ),

            headers={
                "Content-Type":
                "application/x-www-form-urlencoded"
            },

            data={
                "grant_type": "authorization_code",
                "code": code,
                "redirect_uri": self.redirect_uri
            },

            timeout=30
        )

        response.raise_for_status()

        return response.json()


    # -------------------------------------------------
    # 3. Refresh expired access token
    # -------------------------------------------------

    def refresh_access_token(self, refresh_token):

        response = requests.post(
            self.TOKEN_URL,

            auth=(
                self.client_id,
                self.client_secret
            ),

            headers={
                "Content-Type":
                "application/x-www-form-urlencoded"
            },

            data={
                "grant_type": "refresh_token",
                "refresh_token": refresh_token
            },

            timeout=30
        )

        response.raise_for_status()

        return response.json()