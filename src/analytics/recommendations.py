def recommend_action(pin):
    classification = pin["classification"]
    ctr = pin["ctr"]
    engagement_rate = pin["engagement_rate"]

    if classification == "insufficient_data":
        return {
            "action": "collect_more_data",
            "reason": (
                "There is not enough exposure to evaluate this Pin reliably."
            )
        }

    if classification == "winner":
        return {
            "action": "create_more",
            "reason": (
                "This Pin is performing strongly compared with "
                "the other Pins."
            )
        }

    if classification == "laggard" and ctr < 2:
        return {
            "action": "refresh_packaging",
            "reason": (
                "The Pin receives relatively few clicks "
                "after being shown."
            )
        }

    if classification == "laggard" and engagement_rate < 3:
        return {
            "action": "reduce_or_stop",
            "reason": (
                "Overall engagement is relatively low."
            )
        }

    return {
        "action": "continue_testing",
        "reason": (
            "The Pin does not yet provide a strong enough signal "
            "for a major change."
        )
    }