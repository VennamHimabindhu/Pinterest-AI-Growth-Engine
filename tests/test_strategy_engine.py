from src.analytics.strategy_engine import build_strategy_decisions, choose_mode


def test_emerging_trend_explores():
    assert choose_mode("GROWING", None) == "explore"


def test_winner_exploits():
    assert choose_mode(None, "winner") == "exploit"


def test_strategy_creates_trend_experiment():
    trends = [
        {
            "type": "trend_content_opportunity",
            "trend": "skincare",
            "lifecycle": "GROWING",
            "growth": 30,
            "board": "Skincare",
            "board_fit": 1.0,
        }
    ]
    result = build_strategy_decisions([], trends, [])
    assert result[0]["action"] == "create_original_trend_experiment"
    assert result[0]["mode"] == "explore"
