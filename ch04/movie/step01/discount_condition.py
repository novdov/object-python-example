from datetime import datetime

from .discount_conditinon_type import DiscountConditionType


class DiscountCondition:
    def __init__(
        self,
        day_of_week: int,
        start_time: datetime,
        end_time: datetime,
        sequence: int,
        discount_condition_type: DiscountConditionType,
    ):
        self._day_of_week = day_of_week
        self._start_time = start_time
        self._end_time = end_time
        self._sequence = sequence
        self._discount_condition_type = discount_condition_type

    @property
    def discount_condition_type(self):
        return self._discount_condition_type

    @discount_condition_type.setter
    def discount_condition_type(self, discount_condition_type: DiscountConditionType):
        self._discount_condition_type = discount_condition_type

    @property
    def day_of_week(self):
        return self._day_of_week

    @day_of_week.setter
    def day_of_week(self, day_of_week: int):
        self._day_of_week = day_of_week

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, start_time: datetime):
        self._start_time = start_time

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, end_time: datetime):
        self._end_time = end_time

    @property
    def sequence(self):
        return self._sequence

    @sequence.setter
    def sequence(self, sequence: int):
        self._sequence = sequence
