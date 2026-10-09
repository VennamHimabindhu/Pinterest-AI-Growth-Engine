def choose_experiment(pin):
    """
    Decide what kind of experiment should be attempted
    based on the Pin's current performance.
    """

    classification = pin["classification"]
    diagnosis = pin["diagnosis"]

    # No useful data yet
    if classification == "insufficient_data":
        return {
            "experiment_type": "initial_test",
            "change": "creative_variation",
            "reason": (
                "There is not enough performance data yet, "
                "so test an initial creative variation."
            ),
            "goal": "collect_initial_signal"
        }

    # Low CTR but people are saving
    if (
        diagnosis["suggested_change"]
        == "visual_composition"
    ):
        return {
            "experiment_type": "visual_experiment",
            "change": "visual_composition",
            "reason": (
                "The Pin receives saves but relatively few clicks. "
                "Test a stronger visual hook or composition."
            ),
            "goal": "increase_ctr"
        }

    # High CTR but low saves
    if (
        diagnosis["suggested_change"]
        == "content_value"
    ):
        return {
            "experiment_type": "value_experiment",
            "change": "content_value",
            "reason": (
                "The Pin attracts clicks but receives relatively "
                "few saves. Test a more useful or save-worthy concept."
            ),
            "goal": "increase_save_rate"
        }

    # Low overall engagement
    if (
        diagnosis["suggested_change"]
        == "creative_direction"
    ):
        return {
            "experiment_type": "creative_experiment",
            "change": "creative_direction",
            "reason": (
                "Overall engagement is weak. Test a substantially "
                "different creative direction."
            ),
            "goal": "increase_engagement"
        }

    # Winners should still be experimented on
    if classification == "winner":
        return {
            "experiment_type": "winner_variation",
            "change": "creative_variation",
            "reason": (
                "The Pin is performing well, but the system should "
                "continue exploring new creative variations."
            ),
            "goal": "beat_current_champion"
        }

    # Normal Pins continue to be tested
    return {
        "experiment_type": "exploration",
        "change": "creative_variation",
        "reason": (
            "The Pin does not show a strong problem or strong "
            "winning signal. Continue experimentation."
        ),
        "goal": "discover_improvement"
    }