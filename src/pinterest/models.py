from pydantic import BaseModel


class Pin(BaseModel):
    id: str
    title: str | None = None
    description: str | None = None
    board_id: str | None = None


class Board(BaseModel):
    id: str
    name: str | None = None