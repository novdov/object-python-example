"""
사용자들이 에매하는 대상인 '상영'을 구현
"""

from datetime import datetime

from ch02.money import Money

from .customer import Customer
from .movie import Movie
from .reservation import Reservation


class Screening:
    def __init__(self, movie: Movie, sequence: int, when_screened: datetime):
        self._movie = movie
        self._sequence = sequence
        self._when_screened = when_screened

    def reserve(self, customer: Customer, audience_count: int) -> Reservation:
        return Reservation(customer, self, self.calculate_fee(audience_count), audience_count)

    def calculate_fee(self, audience_count: int) -> Money:
        return self._movie.calculate_fee().times(audience_count)

    def get_start_time(self) -> datetime:
        return self._when_screened

    def is_sequence(self, sequence: int) -> bool:
        return self._sequence == sequence

    def get_movie_fee(self):
        return self._movie.get_fee()
