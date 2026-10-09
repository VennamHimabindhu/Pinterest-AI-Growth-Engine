def find_opportunities(board_results):
    opportunities = []

    for board in board_results:

        if board["engagement_rate"] >= 5:
            opportunities.append({
                "type": "high_engagement",
                "board": board["board"],
                "reason": (
                    f"{board['board']} has strong overall engagement "
                    f"at {board['engagement_rate']:.2f}%."
                ),
                "action": "create_more"
            })

        if board["ctr"] >= 3:
            opportunities.append({
                "type": "high_ctr",
                "board": board["board"],
                "reason": (
                    f"{board['board']} generates strong click interest "
                    f"with a CTR of {board['ctr']:.2f}%."
                ),
                "action": "create_click_focused_content"
            })

        if board["save_rate"] >= 4:
            opportunities.append({
                "type": "high_save_rate",
                "board": board["board"],
                "reason": (
                    f"{board['board']} has strong save behavior "
                    f"at {board['save_rate']:.2f}%."
                ),
                "action": "create_save_focused_content"
            })

    return opportunities