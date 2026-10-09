def build_board_context(board):
    """
    Convert Pinterest board information into
    useful context for the content engine.
    """

    board_name = board.get("name", "")
    description = board.get("description", "")

    return {
        "board_id": board["id"],
        "board_name": board_name,
        "board_description": description,
        "board_context": (
            f"Create content specifically for the Pinterest board "
            f"'{board_name}'. "
            f"Keep the topic, wording, keywords, and visual direction "
            f"relevant to this board."
        ),
    }
if __name__ == "__main__":

    board = {
        "id": "1119426119819648286",
        "name": "Korean Skincare",
        "description": "",
    }

    result = build_board_context(board)

    print(result)