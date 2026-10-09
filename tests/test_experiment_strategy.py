from src.analytics.experiment_strategy import choose_experiment


def test_insufficient_data():
    pin = {
        "classification": "insufficient_data",
        "diagnosis": {
            "suggested_change": "collect_more_data"
        }
    }

    result = choose_experiment(pin)

    assert result["experiment_type"] == "initial_test"
    assert result["goal"] == "collect_initial_signal"


def test_low_ctr_high_saves():
    pin = {
        "classification": "laggard",
        "diagnosis": {
            "suggested_change": "visual_composition"
        }
    }

    result = choose_experiment(pin)

    assert result["experiment_type"] == "visual_experiment"
    assert result["change"] == "visual_composition"
    assert result["goal"] == "increase_ctr"


def test_low_engagement():
    pin = {
        "classification": "laggard",
        "diagnosis": {
            "suggested_change": "creative_direction"
        }
    }

    result = choose_experiment(pin)

    assert result["experiment_type"] == "creative_experiment"
    assert result["goal"] == "increase_engagement"


def test_winner_keeps_experimenting():
    pin = {
        "classification": "winner",
        "diagnosis": {
            "suggested_change": "creative_variation"
        }
    }

    result = choose_experiment(pin)

    assert result["experiment_type"] == "winner_variation"
    assert result["goal"] == "beat_current_champion"