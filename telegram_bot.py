import requests

from scraper import EmamiCoinPrice


def format_price_message(coin: EmamiCoinPrice) -> str:
    return (
        "🪙 <b>قیمت زنده سکه امامی</b>\n\n"
        f"💰 قیمت: <b>{coin.price}</b> ریال\n"
        f"📊 تغییر: {coin.change}\n"
        f"📉 کمترین: {coin.low} ریال\n"
        f"📈 بیشترین: {coin.high} ریال\n"
        f"🕐 زمان: {coin.time}\n\n"
        "🔗 <a href='https://www.tgju.org/coin'>tgju.org/coin</a>"
    )


def send_to_channel(token: str, channel_id: str, text: str, timeout: int = 30) -> None:
    response = requests.post(
        f"https://api.telegram.org/bot{token}/sendMessage",
        json={
            "chat_id": channel_id,
            "text": text,
            "parse_mode": "HTML",
            "disable_web_page_preview": True,
        },
        timeout=timeout,
    )
    response.raise_for_status()

    payload = response.json()
    if not payload.get("ok"):
        raise RuntimeError(f"Telegram API error: {payload}")
