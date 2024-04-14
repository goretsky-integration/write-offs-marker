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
            callback_query_id: str,
            text: str,
    ) -> None:
        try:
            await self.__bot.answer_callback_query(
                callback_query_id=callback_query_id,
                text=text,
                show_alert=True,
            )
        except TelegramAPIError:
            logger.exception('Failed to answer callback query')

    async def answer_checkbox_marked(self, callback_query_id: str):
        await self.__answer_checkbox(
            callback_query_id=callback_query_id,
            text='✅ Ингредиент помечен как списанный'
        )

    async def answer_checkbox_could_not_be_marked(self, callback_query_id: str):
        await self.__answer_checkbox(
            callback_query_id=callback_query_id,
            text='❌ Не удалось пометить ингредиент как списанный'
        )
