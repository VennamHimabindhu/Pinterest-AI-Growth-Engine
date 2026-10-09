def normalize_text(text):
    return set(
        word.lower().strip(".,!?")
        for word in text.replace("-", " ").split()
        if word.strip()
    )


def calculate_board_score(topic, board_name):
    topic_words = normalize_text(topic)
    board_words = normalize_text(board_name)

    if not topic_words or not board_words:
        return 0

    matches = topic_words.intersection(board_words)

    return len(matches)


def select_best_board(topic, boards):
    if not boards:
        raise ValueError("No Pinterest boards available.")

    scored_boards = []

    for board in boards:
        score = calculate_board_score(
            topic,
            board["name"]
        )

        scored_boards.append({
            "board_id": board["id"],
            "board_name": board["name"],
            "score": score,
        })

    scored_boards.sort(
        key=lambda board: board["score"],
        reverse=True
    )

    return scored_boards[0]
if __name__ == "__main__":

    import os
    from dotenv import load_dotenv
    from src.pinterest.client import PinterestClient

    load_dotenv()

    token = os.getenv("PINTEREST_ACCESS_TOKEN")

    client = PinterestClient(
        access_token=token
    )

    # Get the user's existing Pinterest boards
    response = client.get(
        "boards",
        params={
            "page_size": 20
        }
    )

    boards = response["items"]

    print(f"Found {len(boards)} existing boards.\n")

    result = select_best_board(
        "Korean skincare routine",
        boards
    )

    print("BEST BOARD:")
    print(result)