from src.database.performance import save_performance
from src.database.connection import get_connection


from src.database.analytics_data import get_pins_for_analytics


pins = get_pins_for_analytics()

print("\nPins for analytics:")

for pin in pins:
    print(pin)
save_performance(
    "1001",
    12000,
    180,
    430
)


connection = get_connection()

try:
    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT
                pin_id,
                impressions,
                clicks,
                saves
            FROM pin_performance
            WHERE pin_id = %s;
            """,
            ("1001",)
        )

        result = cursor.fetchall()

        print("Performance records:")

        for row in result:
            print(row)

finally:
    connection.close()