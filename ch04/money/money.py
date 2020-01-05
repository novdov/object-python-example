from decimal import Decimal


class Money:
    def __init__(self, amount: Decimal):
        self._amount = amount

    @classmethod
    def wons(cls, amount: int) -> "Money":
        return cls(Decimal(amount))

    def plus(self, amount: "Money") -> "Money":
        return Money(self._amount + amount._amount)

    def minus(self, amount: "Money") -> "Money":
        return Money(self._amount - amount._amount)

    def times(self, percent: float) -> "Money":
        return Money(self._amount * percent)

    def is_less_than(self, other: "Money") -> bool:
        return self._amount < other._amount

    def is_greater_than_or_equal(self, other: "Money") -> bool:
        return self._amount >= other._amount

    @classmethod
    def zero(cls):
        return cls.wons(Decimal(0))
