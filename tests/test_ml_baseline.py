from src.analytics.ml_baseline import (
    train_performance_classifier,
    train_engagement_regressor,
)


def test_classifier_is_data_gated():
    result = train_performance_classifier([])
    assert result["status"] == "insufficient_data"


def test_regressor_is_data_gated():
    result = train_engagement_regressor([])
    assert result["status"] == "insufficient_data"
