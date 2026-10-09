from src.analytics.sample_data import pins
from src.analytics.performance import analyze_pin
from src.analytics.ranking import rank_pins


analyzed_pins = [
    analyze_pin(pin)
    for pin in pins
]


ranked_pins = rank_pins(analyzed_pins)


print("\nPIN RANKING")
print("=" * 40)

for position, pin in enumerate(ranked_pins, start=1):

    print(
        f"{position}. "
        f"{pin['title']} "
        f"→ Score: {pin['score']:.2f}"
    )