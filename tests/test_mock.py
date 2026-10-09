from mock_pinterest import mock_pins


print("Pinterest Pins:")

for pin in mock_pins["items"]:
    print(
        f"{pin['id']} - "
        f"{pin['title']} - "
        f"Board: {pin['board_id']}"
    )