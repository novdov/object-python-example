from ch02.money import Money

from ..discount_policy import DiscountPolicy
from ..screening import Screening


class NoneDiscountPolicy(DiscountPolicy):
    def __init__(self):
        super().__init__()

    def get_discount_amount(self, screening: Screening) -> Money:
        return Money.zero()
