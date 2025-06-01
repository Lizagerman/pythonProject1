# external_api.py

import os
from typing import Dict

import requests


def convert_to_rub(amount: float, currency: str) -> float:
    if currency not in ["USD", "EUR"]:
        return amount

    api_key = os.getenv("API_KEY")
    url = f"https://api.apilayer.com/exchangerates_data/latest?base={currency}&symbols=RUB"

    headers = {"apikey": api_key}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        rates = response.json().get("rates", {})
        rub_rate = rates.get("RUB", 1)
        return amount * rub_rate
    else:
        return amount  # Возвращаем исходную сумму, если API не доступ


"""
Модуль для конвертации валюты из USD или EUR в российские рубли (RUB) с использованием API сервиса apilayer.

Требуется установка переменной окружения 'API_KEY' для доступа к API обменных курсов.
"""
