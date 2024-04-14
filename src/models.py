from pydantic import BaseModel

__all__ = ('Event',)


class Event(BaseModel):
    callback_query_id: str
    unit_name: str
    checkbox_a1_coordinates: str
