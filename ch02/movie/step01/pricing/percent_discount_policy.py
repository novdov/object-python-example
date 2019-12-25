from typing import List

from ch02.money import Money

from ..discount_condition import DiscountCondition
from ..discount_policy import DiscountPolicy
from ..screening import Screening


class PercentDiscountPolicy(DiscountPolicy):
    def __init__(self, percent: float, discount_conditions: List[DiscountCondition]):
        super(PercentDiscountPolicy, self).__init__(discount_conditions)
        self._percent = percent

    def get_discount_amount(self, screening: Screening) -> Money:
        return screening.get_movie_fee().times(self._percent)
