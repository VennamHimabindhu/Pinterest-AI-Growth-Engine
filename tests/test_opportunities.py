from src.analytics.sample_data import pins
from src.analytics.board_analysis import analyze_boards
from src.analytics.opportunities import find_opportunities


board_results = analyze_boards(pins)

opportunities = find_opportunities(board_results)


print("\nOPPORTUNITIES")
print("=" * 50)

for opportunity in opportunities:

    print(
        f"\nType: {opportunity['type']}"
    )

    print(
        f"Board: {opportunity['board']}"
    )

    print(
        f"Reason: {opportunity['reason']}"
    )