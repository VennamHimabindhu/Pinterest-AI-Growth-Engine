def calculate_score(
    ctr: float,
    save_rate: float,
    engagement_rate: float
) -> float:

    score = (
        (engagement_rate * 0.50)
        + (ctr * 0.30)
        + (save_rate * 0.20)
    )

    return score


def rank_pins(analyzed_pins):

    for pin in analyzed_pins:

        pin["score"] = calculate_score(
            pin["ctr"],
            pin["save_rate"],
            pin["engagement_rate"]
        )

    return sorted(
        analyzed_pins,
        key=lambda pin: pin["score"],
        reverse=True
    )