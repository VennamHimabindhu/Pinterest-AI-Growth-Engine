def build_content_context(opportunity, board_context=None):

    context = {
        "topic": opportunity["trend"],
        "board": opportunity["board"],
        "trend_growth": opportunity["growth"],
        "goal": opportunity.get(
            "goal",
            "discover_improvement"
        ),
    }

    if board_context:
        context["board_name"] = board_context["board_name"]
        context["board_description"] = board_context["board_description"]
        context["board_context"] = board_context["board_context"]

    return context


if __name__ == "__main__":
    opportunity = {
        "trend": "minimalist skincare",
        "board": "Skincare",
        "growth": 42,
        "goal": "increase_ctr",
    }

    context = build_content_context(opportunity)
    print(context)
