from src.database.pins import save_pin
from src.database.connection import get_connection


pin = {
    "id": "1005",
    "title": "Affordable Beauty Products",
    "description": "Budget-friendly beauty ideas.",
    "board_id": "board_04",
}

save_pin(pin)

connection = get_connection()

try:
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM pins WHERE id = %s",
            ("1005",)
        )

        result = cursor.fetchone()

        print("Saved Pin:")
        print(result)

finally:
    connection.close()