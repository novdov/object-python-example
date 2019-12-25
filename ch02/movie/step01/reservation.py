from ch02.money import Money

from .customer import Customer
from .screening import Screening


class Reservation:
    def __init__(self, customer: Customer, screening: Screening, fee: Money, audience_count: int):
        self._customer = customer
        self._screening = screening
        self._fee = fee
        self._audience_count = audience_count
