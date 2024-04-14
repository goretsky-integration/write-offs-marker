import gspread
from aiogram import Bot
from aiogram.enums import ParseMode
from faststream import Depends
from gspread import Spreadsheet

from config import Config, load_config_from_file
from spreadsheets import SpreadsheetContext
from telegram import TelegramBotContext

__all__ = (
    'get_spreadsheet',
    'get_spreadsheet_context',
    'get_telegram_bot',
    'get_telegram_bot_context',
)


def get_spreadsheet(
        config: Config = Depends(load_config_from_file, use_cache=True),
) -> Spreadsheet:
    service_account = gspread.service_account(
        filename=config.google_sheets_credentials_file_path,
    )
    return service_account.open_by_key(config.spreadsheet_key)


def get_spreadsheet_context(
        spreadsheet: Spreadsheet = Depends(get_spreadsheet),
) -> SpreadsheetContext:
    return SpreadsheetContext(spreadsheet)


async def get_telegram_bot(
        config: Config = Depends(load_config_from_file, use_cache=True),
) -> Bot:
    bot = Bot(
        token=config.telegram_bot_token,
        parse_mode=ParseMode.HTML,
    )
    async with bot.context() as auto_closing_bot:
        yield auto_closing_bot


async def get_telegram_bot_context(bot: Bot = Depends(get_telegram_bot)) -> Bot:
    yield TelegramBotContext(bot)
