from src.analytics.pipeline import run_database_analytics


result = run_database_analytics()


print("\n===== TOP PINS =====")

for pin in result["pins"]:
    print(
        pin["title"],
        "| Score:",
        round(pin["score"], 2),
        "| Performance:",
        pin["performance"]
    )


print("\n===== OPPORTUNITIES =====")

for opportunity in result["opportunities"]:
    print(
        opportunity["type"],
        "|",
        opportunity["board"]
    )