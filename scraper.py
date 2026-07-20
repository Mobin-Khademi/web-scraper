from dataclasses import dataclass

import requests
from bs4 import BeautifulSoup

TGJU_COIN_URL = "https://www.tgju.org/coin"
EMAMI_COIN_SLUG = "sekee"
REQUEST_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "fa-IR,fa;q=0.9",
}


@dataclass(frozen=True)
class EmamiCoinPrice:
    price: str
    change: str
    low: str
    high: str
    time: str

    @property
    def price_normalized(self) -> str:
        return self.price.replace(",", "")


def fetch_emami_coin_price(timeout: int = 30) -> EmamiCoinPrice:
    response = requests.get(TGJU_COIN_URL, headers=REQUEST_HEADERS, timeout=timeout)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    row = soup.find("tr", {"data-market-row": EMAMI_COIN_SLUG})
    if row is None:
        raise ValueError("Emami coin row not found on tgju.org/coin")

    cells = row.find_all("td")
    if len(cells) < 5:
        raise ValueError("Unexpected table structure for Emami coin")

    price = row.get("data-price") or cells[0].get_text(strip=True)

    return EmamiCoinPrice(
        price=price,
        change=cells[1].get_text(strip=True),
        low=cells[2].get_text(strip=True),
        high=cells[3].get_text(strip=True),
        time=cells[4].get_text(strip=True),
    )
