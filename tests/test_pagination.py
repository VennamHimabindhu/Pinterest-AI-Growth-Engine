from mock_pinterest import mock_responses


def get_all_pins():
    all_pins = []

    for response in mock_responses:
        all_pins.extend(response["items"])

        if response["bookmark"] is None:
            break

    return all_pins


pins = get_all_pins()

print(f"Total pins collected: {len(pins)}")

for pin in pins:
    print(f"{pin['id']} - {pin['title']}")