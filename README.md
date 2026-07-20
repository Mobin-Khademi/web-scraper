# Emami Coin Price Telegram Bot

A Python bot that fetches live **Emami coin** prices from [tgju.org](https://www.tgju.org/coin) and automatically posts updates to your Telegram channel.

## Features

- Fetches price, daily change, low, and high
- Sends formatted HTML messages with emojis
- Configurable polling interval
- Optional send-only-on-price-change mode to reduce spam
- Error handling with automatic retry on the next cycle

## Requirements

- Python 3.10 or newer
- A Telegram bot (from [@BotFather](https://t.me/BotFather))
- A Telegram channel where the bot is an **admin**

## Installation

```bash
git clone https://github.com/Mobin-Khademi/webscraper.git
cd webscraper

python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux / macOS
source .venv/bin/activate

pip install -r requirements.txt
```

## Configuration

Copy `.env.example` to `.env` and fill in your values:

```bash
copy .env.example .env
```

| Variable | Description |
|----------|-------------|
| `TELEGRAM_BOT_TOKEN` | Bot token from BotFather |
| `TELEGRAM_CHANNEL_ID` | Channel ID or username (e.g. `@my_channel` or `-1001234567890`) |
| `UPDATE_INTERVAL` | Seconds between price checks (minimum: 10) |
| `SEND_ON_CHANGE_ONLY` | Send a message only when the price changes (`true` / `false`) |

### Channel setup

1. Create a Telegram channel
2. Add your bot to the channel
3. Grant the bot **Post Messages** permission
4. To get `TELEGRAM_CHANNEL_ID`, add [@userinfobot](https://t.me/userinfobot) to the channel or use the Telegram API

## Usage

```bash
python main.py
```

The bot runs continuously and checks the price on each interval, posting to the channel when needed.

## Project structure

```
webscrap/
├── main.py           # Entry point and main loop
├── scraper.py        # Fetches price from tgju.org
├── telegram_bot.py   # Message formatting and Telegram delivery
├── config.py         # Loads settings from .env
├── requirements.txt
├── .env.example
└── README.md
```

## Sample message

```
🪙 Live Emami Coin Price

💰 Price: 45,000,000 IRR
📊 Change: +1.2%
📉 Low: 44,500,000 IRR
📈 High: 45,200,000 IRR
🕐 Time: 14:30:00
```

## Running 24/7 (optional)

For always-on deployment, use tools like `systemd` (Linux), Task Scheduler (Windows), or a cloud hosting service.

## Disclaimer

This project is for educational and personal use only. Review [tgju.org terms](https://www.tgju.org) before use. Changes to the site's HTML structure may break the scraper.

## License

MIT — free to use with attribution.
