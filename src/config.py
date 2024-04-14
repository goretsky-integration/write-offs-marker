import pathlib
import tomllib
from dataclasses import dataclass
from typing import Final

__all__ = ('CONFIG_FILE_PATH', 'load_config_from_file', 'Config')

CONFIG_FILE_PATH: Final[pathlib.Path] = (
        pathlib.Path(__file__).parent.parent / 'config.toml'
)


@dataclass(frozen=True, slots=True)
class Config:
    google_sheets_credentials_file_path: pathlib.Path
    spreadsheet_key: str
    message_queue_url: str
    telegram_bot_token: str


def load_config_from_file(
        file_path: pathlib.Path = CONFIG_FILE_PATH,
) -> Config:
    config_text = file_path.read_text(encoding='utf-8')
    config = tomllib.loads(config_text)

    google_sheets_credentials_file_path = (
        pathlib.Path(config['google_sheets']['credentials_file_path'])
    )
    spreadsheet_key = config['google_sheets']['spreadsheet_key']
    message_queue_url = config['message_queue']['url']
    telegram_bot_token = config['telegram_bot']['token']

    return Config(
        google_sheets_credentials_file_path=google_sheets_credentials_file_path,
        spreadsheet_key=spreadsheet_key,
        message_queue_url=message_queue_url,
        telegram_bot_token=telegram_bot_token,
    )
