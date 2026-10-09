from src.analytics.sample_data import pins
from src.analytics.board_analysis import analyze_boards


results = analyze_boards(pins)


print("\nBOARD ANALYSIS")
print("=" * 50)


for board in results:

    print(f"\nBoard: {board['board']}")
    print(f"Pins: {board['pin_count']}")
    print(f"Impressions: {board['impressions']}")
    print(f"Clicks: {board['clicks']}")
    print(f"Saves: {board['saves']}")
    print(f"CTR: {board['ctr']:.2f}%")
    print(f"Save Rate: {board['save_rate']:.2f}%")
    print(f"Engagement Rate: {board['engagement_rate']:.2f}%")