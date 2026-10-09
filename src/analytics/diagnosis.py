def diagnose_pin(pin):
    ctr = pin["ctr"]
    save_rate = pin["save_rate"]
    engagement_rate = pin["engagement_rate"]
    impressions = pin["impressions"]

    # No exposure means we don't have enough evidence
    if impressions == 0:
        return {
            "observation": "Insufficient data",
            "hypothesis": (
                "The Pin has not received enough exposure "
                "to determine whether the creative is performing well."
            ),
            "suggested_change": "collect_more_data"
        }

    # High saves but low clicks
    if save_rate >= 4 and ctr < 2:
        return {
            "observation": "High saves but low CTR",
            "hypothesis": (
                "The content may be useful enough to save, "
                "but the creative may not encourage clicks."
            ),
            "suggested_change": "visual_composition"
        }

    # High clicks but low saves
    if ctr >= 4 and save_rate < 2:
        return {
            "observation": "High CTR but low saves",
            "hypothesis": (
                "The creative attracts clicks but may not provide "
                "enough value or save-worthy presentation."
            ),
            "suggested_change": "content_value"
        }

    # Low overall engagement
    if engagement_rate < 3:
        return {
            "observation": "Low overall engagement",
            "hypothesis": (
                "The current creative or topic may not be "
                "resonating strongly with the audience."
            ),
            "suggested_change": "creative_direction"
        }

    # No obvious problem
    return {
        "observation": "No strong problem detected",
        "hypothesis": (
            "Continue testing variations to discover improvement."
        ),
        "suggested_change": "creative_variation"
    }