from fast_depends import Depends, inject
from faststream.rabbit import RabbitRouter

from dependencies import get_spreadsheet_context, get_telegram_bot_context
from models import Event
from spreadsheets import SpreadsheetContext
from telegram import TelegramBotContext

__all__ = ('router',)

router = RabbitRouter()


@router.subscriber('write-offs-marker')
@inject
async def on_event(
        event: Event,
        spreadsheet_context: SpreadsheetContext = Depends(
            get_spreadsheet_context,
        ),
        telegram_bot_context: TelegramBotContext = Depends(
            get_telegram_bot_context,
        )
) -> None:
    is_marked = await spreadsheet_context.mark_as_written_off(event)

    if is_marked:
        await telegram_bot_context.answer_checkbox_marked(
            callback_query_id=event.callback_query_id,
            chat_id=event.chat_id,
            message_id=event.message_id,
        )
    else:
        await telegram_bot_context.answer_checkbox_could_not_be_marked(
            callback_query_id=event.callback_query_id,
            chat_id=event.chat_id,
            message_id=event.message_id,
        )
