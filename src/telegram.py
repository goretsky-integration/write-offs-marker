import logging

from aiogram import Bot
from aiogram.exceptions import TelegramAPIError

__all__ = ('TelegramBotContext',)

logger = logging.getLogger('telegram')


class TelegramBotContext:

    def __init__(self, bot: Bot):
        self.__bot = bot

    async def __answer_checkbox(
            self,
            chat_id: int,
            message_id: int,
            callback_query_id: str,
            text: str,
    ) -> None:
        try:
            await self.__bot.answer_callback_query(
                callback_query_id=callback_query_id,
                text=text,
                show_alert=True,
            )
            await self.__bot.edit_message_reply_markup(
                chat_id=chat_id,
                message_id=message_id,
                reply_markup=None,
            )
        except TelegramAPIError:
            logger.exception('Failed to answer callback query')

    async def answer_checkbox_marked(
            self,
            chat_id: int,
            message_id: int,
            callback_query_id: str,
    ):
        await self.__answer_checkbox(
            callback_query_id=callback_query_id,
            chat_id=chat_id,
            message_id=message_id,
            text='✅ Ингредиент помечен как списанный'
        )

    async def answer_checkbox_could_not_be_marked(
            self,
            chat_id: int,
            message_id: int,
            callback_query_id: str,
    ):
        await self.__answer_checkbox(
            callback_query_id=callback_query_id,
            chat_id=chat_id,
            message_id=message_id,
            text='❌ Не удалось пометить ингредиент как списанный'
        )
