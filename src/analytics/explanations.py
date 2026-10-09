def explain_score(pin):
    engagement_contribution = pin["engagement_rate"] * 0.50
    ctr_contribution = pin["ctr"] * 0.30
    save_contribution = pin["save_rate"] * 0.20

    return {
        "engagement_contribution": engagement_contribution,
        "ctr_contribution": ctr_contribution,
        "save_contribution": save_contribution,
    }