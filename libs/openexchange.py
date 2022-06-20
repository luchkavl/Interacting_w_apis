import requests
from cachetools import cached, TTLCache


class OpenExchangeClient:
    BASE_URL = 'https://openexchangerates.org/api/'

    def __init__(self, app_id):
        self.app_id = app_id

    @property
    @cached(cache=TTLCache(maxsize=2, ttl=900))
    def latest_rates(self):
        return requests.get(f'{self.BASE_URL}/latest.json?app_id={self.app_id}').json()

    def convert(self, amount, from_curr, to_curr):
        rates = self.latest_rates['rates']
        to_rate = rates[to_curr]

        if from_curr == 'USD':
            return amount * to_rate
        else:
            from_in_usd = amount / rates[from_curr]
            return from_in_usd * to_rate
