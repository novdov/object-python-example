from ..discount_condition import DiscountCondition
from ..screening import Screening


class SequenceCondition(DiscountCondition):
    def __init__(self, sequence: int):
        super(SequenceCondition, self).__init__()
        self._sequence = sequence

    def is_satisfied_by(self, screening: Screening) -> bool:
        return screening.is_sequence(self._sequence)
