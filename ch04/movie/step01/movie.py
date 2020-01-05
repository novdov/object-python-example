import pprint
from datetime import timedelta
from typing import List

from ch04.money import Money

from .discount_condition import DiscountCondition
from .movie_type import MovieType


class Movie:
    """
    데이터 중심의 객체 설계
    """

    def __init__(
        self,
        title: str,
        running_time: timedelta,
        fee: Money,
        discount_amount: Money,
        discount_percent: float,
        discount_conditions: List[DiscountCondition],
        movie_type: MovieType = MovieType.NONE_DISCOUNT,
    ):
        self._title = title
        self._running_time = running_time
        self._fee = fee
        self._discount_amount = discount_amount
        self._discount_percent = discount_percent
        self._discount_conditions = discount_conditions
        self._movie_type = movie_type

        self._cls_args = locals()
        self._movie_type_args = {
            MovieType.NONE_DISCOUNT: {"discount_amount": Money.zero(), "discount_percent": 0,},
            MovieType.PERCENT_DISCOUNT: {"discount_amount": Money.zero(),},
            MovieType.AMOUNT_DISCOUNT: {"discount_percent": 0,},
        }
        self._validate_args()

    def _validate_args(self):
        _args_dict = self._movie_type_args[self._movie_type]
        for name, value in locals().items():
            if name in _args_dict and value != _args_dict[name]:
                raise ValueError(
                    f"Expected values: {self._movie_type}: {pprint.pformat(_args_dict, indent=2)}, "
                    f"but got [{name}:{value}]"
                )

    @property
    def movie_type(self):
        return self._movie_type

    @movie_type.setter
    def movie_type(self, movie_type: MovieType):
        self._movie_type = movie_type

    @property
    def fee(self):
        return self._fee

    @fee.setter
    def fee(self, fee: Money):
        self._fee = fee

    @property
    def discount_conditions(self):
        return self._discount_conditions

    @discount_conditions.setter
    def discount_conditions(self, discount_conditions: List[DiscountCondition]):
        self._discount_conditions = discount_conditions

    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount: Money):
        self._discount_amount = discount_amount

    @property
    def discount_percent(self):
        return self._discount_percent

    @discount_percent.setter
    def discount_percent(self, discount_percent: float):
        self._discount_percent = discount_percent
