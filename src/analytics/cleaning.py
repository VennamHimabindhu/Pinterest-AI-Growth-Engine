def clean_pin(pin):
    cleaned = pin.copy()

    # Clean title
    if not cleaned.get("title"):
        cleaned["title"] = "Untitled Pin"

    # Clean numeric fields
    numeric_fields = [
        "impressions",
        "clicks",
        "saves"
    ]

    for field in numeric_fields:
        value = cleaned.get(field)

        if value is None or value == "":
            cleaned[field] = 0
        else:
            cleaned[field] = int(value)

    return cleaned


def clean_pins(pins):
    cleaned_pins = []

    for pin in pins:
        if not pin.get("id"):
            continue

        cleaned_pins.append(clean_pin(pin))

    return cleaned_pins