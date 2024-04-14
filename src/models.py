from pydantic import BaseModel

__all__ = ('Event',)


class Event(BaseModel):
    callback_query_id: str
    chat_id: int
    message_id: int
    unit_name: str
    checkbox_a1_coordinates: str
