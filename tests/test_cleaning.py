from src.analytics.cleaning import clean_pins


dirty_pins = [
    {
        "id": "2001",
        "title": "",
        "impressions": "10000",
        "clicks": None,
        "saves": "250",
    },
    {
        "id": "2002",
        "title": "Hair Tips",
        "impressions": 5000,
        "clicks": 100,
        "saves": 50,
    }
]


cleaned = clean_pins(dirty_pins)

for pin in cleaned:
    print(pin)