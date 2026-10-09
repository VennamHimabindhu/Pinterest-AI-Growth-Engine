from src.pinterest.models import Pin


# This represents a Pinterest API response
api_response = {
    "items": [
        {
            "id": "1001",
            "title": "Budget Skincare Routine",
            "description": "Affordable skincare ideas",
            "board_id": "board_01"
        },
        {
            "id": "1002",
            "title": "Simple Morning Skincare",
            "description": "Easy skincare routine",
            "board_id": "board_01"
        }
    ],
    "bookmark": None
}


# Convert each API item into our Pin model
pins = [
    Pin(**item)
    for item in api_response["items"]
]


print(f"Pins received: {len(pins)}")

for pin in pins:
    print(f"\nID: {pin.id}")
    print(f"Title: {pin.title}")
    print(f"Board: {pin.board_id}")