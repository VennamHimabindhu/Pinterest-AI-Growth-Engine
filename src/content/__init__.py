def build_content_context(opportunity):
    return {
        "topic": opportunity["trend"],
        "board": opportunity["board"],
        "trend_growth": opportunity["growth"],
        "goal": opportunity.get("goal", "discover_improvement"),
    }

if __name__ == "__main__":
    opportunity = {
        "trend": "minimalist skincare",
        "board": "Skincare",
        "growth": 42,
        "goal": "increase_ctr",
    }

    context = build_content_context(opportunity)

    print(context)