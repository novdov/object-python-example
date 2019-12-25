from datetime import datetime

from ..discount_condition import DiscountCondition
from ..screening import Screening


class PeriodCondition(DiscountCondition):
    def __init__(self, day_of_week: int, start_time: datetime, end_time: datetime):
        super(PeriodCondition, self).__init__()
        self._day_of_week = day_of_week
        self._start_time = start_time
        self._end_time = end_time

    def is_satisfied_by(self, screening: Screening) -> bool:
        conditions = [
            screening.get_start_time().weekday() == self._day_of_week,
            self._start_time <= screening.get_start_time() <= self._end_time,
        ]
        return all(conditions)
