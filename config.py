import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    telegram_bot_token: str
    telegram_channel_id: str
    update_interval: int
    send_on_change_only: bool


def load_settings() -> Settings:
    token = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
    channel_id = os.getenv("TELEGRAM_CHANNEL_ID", "").strip()

    if not token:
        raise ValueError("TELEGRAM_BOT_TOKEN is not set in .env")
    if not channel_id:
        raise ValueError("TELEGRAM_CHANNEL_ID is not set in .env")

    interval = int(os.getenv("UPDATE_INTERVAL", "60"))
    send_on_change_only = os.getenv("SEND_ON_CHANGE_ONLY", "true").lower() in {
        "1",
        "true",
        "yes",
    }

    return Settings(
        telegram_bot_token=token,
        telegram_channel_id=channel_id,
        update_interval=max(interval, 10),
        send_on_change_only=send_on_change_only,
    )
