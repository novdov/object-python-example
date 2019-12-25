from typing import List

from ch02.money import Money

from ..discount_condition import DiscountCondition
from ..discount_policy import DiscountPolicy
from ..screening import Screening


class AmountDiscountPolicy(DiscountPolicy):
    def __init__(self, discount_amount: Money, discount_conditions: List[DiscountCondition]):
        super(AmountDiscountPolicy, self).__init__(discount_conditions)
        self._discount_amount = discount_amount

    def get_discount_amount(self, screening: Screening) -> Money:
        return self._discount_amount
