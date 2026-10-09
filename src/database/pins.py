from src.database.connection import get_connection


def save_pin(pin):
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO pins (
                    id,
                    title,
                    description,
                    board_id
                )
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (id)
                DO UPDATE SET
                    title = EXCLUDED.title,
                    description = EXCLUDED.description,
                    board_id = EXCLUDED.board_id;
                """,
                (
                    pin["id"],
                    pin.get("title"),
                    pin.get("description"),
                    pin.get("board_id"),
                ),
            )

        connection.commit()

    finally:
        connection.close()


def save_pins(pins):
    for pin in pins:
        save_pin(pin)