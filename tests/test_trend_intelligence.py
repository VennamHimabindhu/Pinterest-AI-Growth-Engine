from src.analytics.trend_intelligence import (
    classify_lifecycle,
    trend_board_fit,
    detect_emerging_topics,
    build_trend_opportunities,
)


def test_growing_lifecycle():
    assert classify_lifecycle(35) == "GROWING"


def test_board_fit():
    assert trend_board_fit("skincare routine", "Skincare") > 0


def test_emerging_topics():
    trends = [
        {"keyword": "skincare", "pct_growth_wow": 30, "region": "US", "source": "test"},
        {"keyword": "old topic", "pct_growth_wow": -25, "region": "US", "source": "test"},
    ]
    result = detect_emerging_topics(trends)
    assert len(result) == 1
    assert result[0]["keyword"] == "skincare"


def test_trend_opportunity():
    trends = [
        {
            "keyword": "skincare",
            "pct_growth_wow": 30,
            "region": "US",
            "source": "test",
        }
    ]
    boards = [{"board": "Skincare", "ctr": 2, "engagement_rate": 5}]
    result = build_trend_opportunities(trends, boards)
    assert result
    assert result[0]["trend"] == "skincare"
