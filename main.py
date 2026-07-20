import logging
import sys
import time

from config import load_settings
from scraper import fetch_emami_coin_price
from telegram_bot import format_price_message, send_to_channel

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


def main() -> None:
    try:
        settings = load_settings()
    except ValueError as exc:
        logger.error("%s", exc)
        logger.error("Copy .env.example to .env and fill in your values.")
        sys.exit(1)

    last_price: str | None = None
    logger.info("Bot started. Checking every %s seconds.", settings.update_interval)

    while True:
        try:
            coin = fetch_emami_coin_price()
            should_send = not settings.send_on_change_only or coin.price_normalized != last_price

            if should_send:
                message = format_price_message(coin)
                send_to_channel(
                    settings.telegram_bot_token,
                    settings.telegram_channel_id,
                    message,
                )
                last_price = coin.price_normalized
                logger.info("Sent price update: %s", coin.price)
            else:
                logger.info("Price unchanged: %s", coin.price)

        except Exception:
            logger.exception("Failed to fetch or send price update")

        time.sleep(settings.update_interval)


if __name__ == "__main__":
    main()
