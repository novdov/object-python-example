import abc

from .screening import Screening


class DiscountCondition(abc.ABC):
    def __init__(self):
        pass

    @abc.abstractmethod
    def is_satisfied_by(self, screening: Screening) -> bool:
        return NotImplementedError
