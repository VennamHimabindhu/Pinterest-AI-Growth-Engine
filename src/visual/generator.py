from pathlib import Path


class ImageGenerator:

    def generate(self, image_prompt):
        raise NotImplementedError(
            "Image generation is not implemented yet."
        )


class MockImageGenerator(ImageGenerator):

    def generate(self, image_prompt):
        output_dir = Path("generated_images")
        output_dir.mkdir(exist_ok=True)

        image_path = output_dir / "mock_image.txt"

        image_path.write_text(
            f"Mock image generated from prompt:\n\n{image_prompt}",
            encoding="utf-8",
        )

        return {
            "status": "success",
            "asset_type": "mock",
            "image_path": str(image_path),
            "prompt": image_prompt,
        }


class CloudImageGenerator(ImageGenerator):

    def __init__(self):
        from dotenv import load_dotenv
        import os

        load_dotenv()

        self.api_key = os.getenv("POLLINATIONS_API_KEY")

        if not self.api_key:
            raise ValueError(
                "POLLINATIONS_API_KEY is missing from .env"
            )

    def generate(self, image_prompt):
        import requests
        from pathlib import Path
        from urllib.parse import quote

        output_dir = Path("generated_images")
        output_dir.mkdir(exist_ok=True)

        encoded_prompt = quote(image_prompt)

        url = (
            f"https://gen.pollinations.ai/image/"
            f"{encoded_prompt}"
        )

        response = requests.get(
            url,
            headers={
                "Authorization": f"Bearer {self.api_key}"
            },
            params={
                "model": "flux",
            },
            timeout=120,
        )

        response.raise_for_status()

        image_path = output_dir / "generated_image.jpg"

        image_path.write_bytes(response.content)

        return {
            "status": "success",
            "asset_type": "cloud",
            "image_path": str(image_path),
            "prompt": image_prompt,
        }


if __name__ == "__main__":

    generator = CloudImageGenerator()

    result = generator.generate(
        "Minimalist skincare routine on a wooden table"
    )

    print(result)