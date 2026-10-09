from src.pinterest.models import Pin, Board


pin = Pin(
    id="1001",
    title="Budget Skincare Routine",
    description="Affordable skincare ideas",
    board_id="board_01"
)

board = Board(
    id="board_01",
    name="Skincare"
)

print("PIN")
print(pin)

print("\nBOARD")
print(board)