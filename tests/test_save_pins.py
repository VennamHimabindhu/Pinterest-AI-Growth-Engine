from src.database.pins import save_pins
from src.database.connection import get_connection


pins = [
    {
        "id": "2001",
        "title": "Morning Skincare",
        "description": "Simple morning routine.",
        "board_id": "board_01",
    },
    {
        "id": "2002",
        "title": "Healthy Hair Tips",
        "description": "Easy hair-care ideas.",
        "board_id": "board_02",
    },
    {
        "id": "2003",
        "title": "Self Care Ideas",
        "description": "Simple self-care ideas.",
        "board_id": "board_03",
    },
]

save_pins(pins)

connection = get_connection()

try:
    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT id, title, board_id
            FROM pins
            WHERE id IN ('2001', '2002', '2003')
            ORDER BY id;
            """
        )

        for row in cursor.fetchall():
            print(row)

finally:
    connection.close()