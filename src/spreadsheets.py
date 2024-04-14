import asyncio

from gspread import Spreadsheet
from gspread.utils import ValueInputOption

from models import Event

__all__ = ('SpreadsheetContext',)


class SpreadsheetContext:

    def __init__(self, spreadsheet: Spreadsheet):
        self.__spreadsheet = spreadsheet

    async def mark_as_written_off(self, event: Event) -> bool:
        result = await asyncio.to_thread(
            self.__spreadsheet.values_update,
            range=f'{event.unit_name}!{event.checkbox_a1_coordinates}',
            params={'valueInputOption': ValueInputOption.user_entered},
            body={'values': [['TRUE']]}
        )
        return result.get('updatedCells') == 1
