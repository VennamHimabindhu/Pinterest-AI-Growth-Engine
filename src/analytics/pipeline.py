from src.analytics.cleaning import clean_pins
from src.analytics.performance import analyze_pin
from src.analytics.ranking import rank_pins
from src.analytics.board_analysis import analyze_boards
from src.analytics.opportunities import find_opportunities

from src.analytics.classification import (
    calculate_percentile,
    classify_performance,
    get_data_status,
)

from src.analytics.features import create_features
from src.analytics.explanations import explain_score
from src.analytics.recommendations import recommend_action
from src.analytics.diagnosis import diagnose_pin
from src.analytics.experiment_strategy import choose_experiment

from src.analytics.trend_intelligence import (
    build_trend_opportunities,
    detect_emerging_topics,
    analyze_creative_patterns,
)
from src.analytics.strategy_engine import build_strategy_decisions
from src.analytics.ml_baseline import (
    train_performance_classifier,
    train_engagement_regressor,
)

from src.analytics.trend_provider import MockTrendProvider
from src.database.analytics_data import get_pins_for_analytics


def run_analytics(
    pins,
    trend_provider=None,
    creative_evidence=None,
):
    cleaned_pins = clean_pins(pins)

    analyzed_pins = [
        analyze_pin(pin)
        for pin in cleaned_pins
    ]

    ranked_pins = rank_pins(analyzed_pins)

    comparable_pins = [
        pin for pin in ranked_pins
        if pin["impressions"] >= 1000
    ]

    comparable_scores = [
        pin["score"] for pin in comparable_pins
    ]

    for pin in ranked_pins:
        data_status = get_data_status(pin["impressions"])
        pin["data_status"] = data_status

        if pin["impressions"] >= 1000 and comparable_scores:
            percentile = calculate_percentile(
                pin["score"],
                comparable_scores,
            )
        else:
            percentile = None

        pin["percentile"] = percentile

        if percentile is not None:
            pin["classification"] = classify_performance(
                percentile,
                pin["impressions"],
            )
        else:
            pin["classification"] = data_status

        pin["features"] = create_features(pin)
        pin["score_explanation"] = explain_score(pin)
        pin["recommendation"] = recommend_action(pin)
        pin["diagnosis"] = diagnose_pin(pin)
        pin["experiment"] = choose_experiment(pin)

    board_results = analyze_boards(cleaned_pins)
    opportunities = find_opportunities(board_results)

    # Development mode uses clearly labeled mock trend data.
    # Replace with PinterestTrendsAPIProvider after approved access exists.
    trend_provider = trend_provider or MockTrendProvider()
    raw_trends = trend_provider.get_trending_keywords(
        region="US",
        trend_type="growing",
        limit=10,
    )

    trends = detect_emerging_topics(raw_trends)
    trend_opportunities = build_trend_opportunities(
        trends,
        board_results,
    )

    creative_patterns = analyze_creative_patterns(
        creative_evidence or []
    )

    strategy_decisions = build_strategy_decisions(
        ranked_pins,
        trend_opportunities,
        creative_patterns,
    )

    # ML is deliberately advisory and data-gated.
    classifier = train_performance_classifier(ranked_pins)
    regressor = train_engagement_regressor(ranked_pins)

    return {
        "pins": ranked_pins,
        "boards": board_results,
        "opportunities": opportunities,
        "trends": trends,
        "trend_opportunities": trend_opportunities,
        "creative_patterns": creative_patterns,
        "strategy_decisions": strategy_decisions,
        "ml": {
            "classifier": classifier,
            "regressor": regressor,
        },
    }


def run_database_analytics():
    pins = get_pins_for_analytics()
    return run_analytics(pins)


if __name__ == "__main__":
    result = run_database_analytics()

    print("\n===== WEEK 4 INTELLIGENCE ENGINE =====")

    for pin in result["pins"]:
        print("\n------------------------------")
        print("PIN:", pin["id"])
        print("Title:", pin["title"])
        print("Impressions:", pin["impressions"])
        print("Clicks:", pin["clicks"])
        print("Saves:", pin["saves"])
        print("Score:", pin["score"])
        print("Data Status:", pin["data_status"])
        print("Percentile:", pin["percentile"])
        print("Classification:", pin["classification"])
        print("Diagnosis:", pin["diagnosis"])
        print("Recommendation:", pin["recommendation"])
        print("Experiment:", pin["experiment"])

    print("\n===== TREND OPPORTUNITIES =====")
    for item in result["trend_opportunities"]:
        print(item)

    print("\n===== STRATEGY DECISIONS =====")
    for decision in result["strategy_decisions"]:
        print(decision)

    print("\n===== ML STATUS =====")
    print(result["ml"])
