def create_experiment(
    pin,
    observation,
    hypothesis,
    change_type,
    expected_outcome
):
    return {
        "pin_id": pin["id"],
        "board": pin.get("board"),
        "observation": observation,
        "hypothesis": hypothesis,
        "change_type": change_type,
        "expected_outcome": expected_outcome,
        "status": "proposed",
    }