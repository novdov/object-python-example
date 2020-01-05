import enum


class MovieType(enum.Enum):
    AMOUNT_DISCOUNT = enum.auto()
    PERCENT_DISCOUNT = enum.auto()
    NONE_DISCOUNT = enum.auto()
