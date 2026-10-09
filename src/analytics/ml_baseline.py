from __future__ import annotations

from typing import Any

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split


FEATURE_NAMES = [
    "impressions",
    "clicks",
    "saves",
    "ctr",
    "save_rate",
    "engagement_rate",
]


def _features(pin: dict[str, Any]) -> list[float]:
    return [float(pin.get(name, 0) or 0) for name in FEATURE_NAMES]


def train_performance_classifier(
    pins: list[dict[str, Any]],
    min_samples: int = 20,
) -> dict[str, Any]:
    """
    ML is a later-stage learner, not the primary decision engine yet.
    With the current tiny prototype dataset this intentionally returns
    insufficient_data instead of pretending the model is reliable.
    """
    labeled = [
        pin
        for pin in pins
        if pin.get("classification") in {"winner", "laggard", "normal"}
    ]

    labels = [pin["classification"] for pin in labeled]

    if len(labeled) < min_samples or len(set(labels)) < 2:
        return {
            "status": "insufficient_data",
            "reason": (
                f"Need at least {min_samples} labeled Pins and at least "
                "two classes before training a useful classifier."
            ),
            "model": None,
        }

    X = np.array([_features(pin) for pin in labeled])
    y = np.array(labels)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y,
    )

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42,
        class_weight="balanced",
    )
    model.fit(X_train, y_train)

    train_accuracy = accuracy_score(y_train, model.predict(X_train))
    test_accuracy = accuracy_score(y_test, model.predict(X_test))

    gap = train_accuracy - test_accuracy

    return {
        "status": "trained",
        "model": model,
        "train_accuracy": round(train_accuracy, 3),
        "test_accuracy": round(test_accuracy, 3),
        "possible_overfitting": gap > 0.20,
        "train_test_gap": round(gap, 3),
    }


def train_engagement_regressor(
    pins: list[dict[str, Any]],
    min_samples: int = 20,
) -> dict[str, Any]:
    """
    Baseline regression for predicting engagement rate.
    The output is advisory; actual performance remains the ground truth.
    """
    usable = [
        pin
        for pin in pins
        if float(pin.get("impressions", 0) or 0) > 0
    ]

    if len(usable) < min_samples:
        return {
            "status": "insufficient_data",
            "reason": f"Need at least {min_samples} usable Pins for regression.",
            "model": None,
        }

    X = np.array([_features(pin) for pin in usable])
    y = np.array(
        [float(pin.get("engagement_rate", 0) or 0) for pin in usable]
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    train_r2 = r2_score(y_train, model.predict(X_train))
    test_r2 = r2_score(y_test, model.predict(X_test))
    mae = mean_absolute_error(y_test, model.predict(X_test))

    gap = train_r2 - test_r2

    return {
        "status": "trained",
        "model": model,
        "train_r2": round(train_r2, 3),
        "test_r2": round(test_r2, 3),
        "test_mae": round(mae, 3),
        "possible_overfitting": gap > 0.20,
        "train_test_gap": round(gap, 3),
    }
