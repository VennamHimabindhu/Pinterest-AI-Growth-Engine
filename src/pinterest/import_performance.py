import os

from dotenv import load_dotenv

from src.pinterest.client import PinterestClient
from src.pinterest.performance import extract_pin_performance
from src.database.pins import save_pins
from src.database.performance import save_performance_batch


load_dotenv()


def import_pin_performance():
    token = os.getenv("PINTEREST_ACCESS_TOKEN")

    client = PinterestClient(access_token=token)

    result = client.get(
        "pins",
        params={
            "page_size": 20,
            "pin_metrics": "true",
        },
    )

    pins = result.get("items", [])

    # Step 1: Save the Pins first
    save_pins(pins)

    # Step 2: Extract their performance metrics
    records = []

    for pin in pins:
        pin_records = extract_pin_performance(pin)
        records.extend(pin_records)

    # Step 3: Save performance metrics
    if records:
        save_performance_batch(records)

    return records


if __name__ == "__main__":
    records = import_pin_performance()

    print(f"Imported {len(records)} performance records.")

    for record in records:
        print(record)