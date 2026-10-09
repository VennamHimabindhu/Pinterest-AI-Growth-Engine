import os
import base64
import requests
from dotenv import load_dotenv

load_dotenv()


class PinterestPublisher:

    # Sandbox API for testing
    BASE_URL = "https://api-sandbox.pinterest.com/v5"

    def __init__(self):
        self.access_token = os.getenv(
            "PINTEREST_SANDBOX_ACCESS_TOKEN"
        )

        if not self.access_token:
            raise ValueError(
                "PINTEREST_SANDBOX_ACCESS_TOKEN is missing from .env"
            )

        self.headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json",
        }

    def create_pin(
        self,
        board_id,
        title,
        description,
        image_path,
        link=None,
    ):
        with open(image_path, "rb") as image_file:
            image_base64 = base64.b64encode(
                image_file.read()
            ).decode("utf-8")

        payload = {
            "board_id": board_id,
            "title": title,
            "description": description,
            "media_source": {
                "source_type": "image_base64",
                "content_type": "image/jpeg",
                "data": image_base64,
            },
        }

        if link:
            payload["link"] = link

        response = requests.post(
            f"{self.BASE_URL}/pins",
            headers=self.headers,
            json=payload,
            timeout=60,
        )

        if not response.ok:
            print("\n========== PINTEREST ERROR ==========")
            print("STATUS:", response.status_code)
            print("RESPONSE:", response.text)
            print("=====================================\n")

        response.raise_for_status()
        return response.json()


if __name__ == "__main__":

    publisher = PinterestPublisher()

    # This must be a Sandbox board ID, not a production board ID.
    result = publisher.create_pin(
        board_id="1119426119819784344",
        title="Minimalist Korean Skincare Routine",
        description=(
            "A simple and calming Korean skincare routine "
            "focused on a minimalist approach."
        ),
        image_path="generated_images/generated_image.jpg",
    )

    print("\n========== SANDBOX PIN CREATED ==========")
    print(result)