import abc
from typing import List, Optional

from ch02.money import Money

from .discount_condition import DiscountCondition
from .screening import Screening


class DiscountPolicy(abc.ABC):
    def __init__(self, conditions: Optional[List[DiscountCondition]] = None):
        self._conditions = conditions

    def calculate_discount_amount(self, screening: Screening) -> Money:
        for condition in self._conditions:
            if condition.is_satisfied_by(screening):
                return self.get_discount_amount(screening)
        return Money.zero()

    @abc.abstractmethod
    def get_discount_amount(self, screening: Screening) -> Money:
        return NotImplementedError
