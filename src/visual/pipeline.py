import os
from dotenv import load_dotenv

from src.content.pipeline import run_content_pipeline
from src.visual.prompt import (
    build_visual_spec,
    build_image_generation_prompt,
)
from src.visual.generator import CloudImageGenerator
from src.pinterest.board_selector import select_best_board
from src.pinterest.client import PinterestClient
from src.pinterest.publisher import PinterestPublisher


load_dotenv()

# Sandbox board created earlier for testing.
SANDBOX_BOARD_ID = "1119426119819784344"


def get_existing_boards():
    """Fetch real Pinterest boards for board selection."""

    token = os.getenv("PINTEREST_ACCESS_TOKEN")

    if not token:
        raise ValueError(
            "PINTEREST_ACCESS_TOKEN is missing from .env"
        )

    client = PinterestClient(access_token=token)

    response = client.get(
        "boards",
        params={"page_size": 20},
    )

    return response.get("items", [])


def build_visual_pipeline(opportunity):
    # 1. Fetch existing production boards for topic matching.
    boards = get_existing_boards()

    if not boards:
        raise ValueError("No existing Pinterest boards were found.")

    print(f"Found {len(boards)} existing Pinterest boards.")

    # 2. Select the most relevant existing board.
    selected_board = select_best_board(
        opportunity["trend"],
        boards,
    )

    print("\n========== SELECTED PRODUCTION BOARD ==========")
    print("Name:", selected_board["board_name"])
    print("ID:", selected_board["board_id"])
    print("Score:", selected_board["score"])

    # 3. Find the selected board's full details.
    board = next(
        (
            item
            for item in boards
            if item["id"] == selected_board["board_id"]
        ),
        None,
    )

    if board is None:
        raise ValueError("Selected board could not be found.")

    board_context = {
        "board_id": board["id"],
        "board_name": board.get("name", ""),
        "board_description": board.get("description", ""),
        "board_context": (
            f"Create content specifically for the Pinterest board "
            f"'{board.get('name', '')}'. Make the topic, wording, "
            f"keywords, and visual direction relevant to this board."
        ),
    }

    # 4. Generate and evaluate Pin content.
    content_result = run_content_pipeline(
        opportunity,
        board_context=board_context,
    )

    if content_result["status"] != "approved":
        return {
            "status": "rejected",
            "reason": "Content validation failed.",
            "board": selected_board,
            "content": content_result.get("content"),
            "visual_spec": None,
            "image": None,
        }

    content = content_result["content"]

    # 5. Build the structured visual specification.
    visual_spec = build_visual_spec(content)

    # 6. Build the final image-generation prompt.
    final_image_prompt = build_image_generation_prompt(
        visual_spec
    )

    # 7. Generate the real image.
    generator = CloudImageGenerator()
    image = generator.generate(final_image_prompt)

    if not image or image.get("status") != "success":
        return {
            "status": "image_generation_failed",
            "reason": "The image generator did not return a successful image.",
            "board": selected_board,
            "content": content,
            "visual_spec": visual_spec,
            "image": image,
        }

    image_path = image.get("image_path")

    if not image_path or not os.path.isfile(image_path):
        return {
            "status": "image_generation_failed",
            "reason": "The generated image file could not be found.",
            "board": selected_board,
            "content": content,
            "visual_spec": visual_spec,
            "image": image,
        }

    # 8. Return the complete approved Pin candidate.
    return {
        "status": "approved",
        "board": selected_board,
        "board_context": board_context,
        "content": content,
        "visual_spec": visual_spec,
        "image_prompt": final_image_prompt,
        "image": image,
    }


if __name__ == "__main__":
    opportunity = {
        "trend": "minimalist skincare",
        "board": "Skincare",
        "growth": 42,
        "goal": "increase_ctr",
    }

    # Generate content and image.
    result = build_visual_pipeline(opportunity)

    print("\n========== STATUS ==========")
    print(result["status"])

    if result["status"] != "approved":
        print("\nPipeline stopped safely.")
        print("Reason:", result.get("reason", "Content was not approved."))
        raise SystemExit(1)

    content = result["content"]
    image = result["image"]

    print("\n========== SELECTED BOARD ==========")
    print(result["board"])

    print("\n========== TITLE ==========")
    print(content.title)

    print("\n========== DESCRIPTION ==========")
    print(content.description)

    print("\n========== IMAGE ==========")
    print(image)

    print("\n========== PUBLISHING MODE ==========")
    print("SANDBOX")
    print("Sandbox board ID:", SANDBOX_BOARD_ID)

    # 9. Ask for explicit confirmation before creating a Sandbox Pin.
    publish = input(
        "\nPublish this Pin to the SANDBOX board? (yes/no): "
    ).strip().lower()

    if publish != "yes":
        print("Pin not published.")
        raise SystemExit(0)

    # 10. Publish using the Sandbox publisher and Sandbox board ID.
    publisher = PinterestPublisher()

    try:
        published_pin = publisher.create_pin(
            board_id=SANDBOX_BOARD_ID,
            title=content.title,
            description=content.description,
            image_path=image["image_path"],
        )

        print("\n========== SANDBOX PIN CREATED ==========")
        print("Pin ID:", published_pin.get("id"))
        print("Board ID:", published_pin.get("board_id"))
        print("Title:", published_pin.get("title"))

    except Exception as error:
        print("\nSandbox publishing failed.")
        print("Error:", error)
        raise SystemExit(1)