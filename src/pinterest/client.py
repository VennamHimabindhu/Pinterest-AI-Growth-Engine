import requests


class PinterestAPIError(Exception):
    """Custom error for Pinterest API problems."""
    pass


class PinterestClient:

    BASE_URL = "https://api.pinterest.com/v5"

    def __init__(self, access_token=None):
        self.access_token = access_token

    def get(self, endpoint, params=None):

        url = f"{self.BASE_URL}/{endpoint}"

        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json",
        }

        try:
            response = requests.get(
                url,
                headers=headers,
                params=params,
                timeout=30,
            )

            if response.status_code == 401:
                raise PinterestAPIError(
                    "401 Unauthorized: Check your access token."
                )

            if response.status_code == 403:
                raise PinterestAPIError(
                    "403 Forbidden: Your app does not have permission."
                )

            if response.status_code == 404:
                raise PinterestAPIError(
                    "404 Not Found: The requested Pinterest resource does not exist."
                )

            if response.status_code == 429:
                raise PinterestAPIError(
                    "429 Too Many Requests: Pinterest rate limit reached."
                )

            response.raise_for_status()

            return response.json()

        except requests.RequestException as error:
            raise PinterestAPIError(
                f"Pinterest request failed: {error}"
            )
if __name__ == "__main__":
    import os
    from dotenv import load_dotenv

    load_dotenv()

    token = os.getenv("PINTEREST_ACCESS_TOKEN")

    client = PinterestClient(access_token=token)

    result = client.get(
    "pins",
    params={
        "page_size": 20,
        "pin_metrics": "true",
    },
)

    print(result)