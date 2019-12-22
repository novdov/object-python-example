from .bag import Bag
from .ticket import Ticket


class Audience:
    def __init__(self, bag: Bag):
        self._bag = bag

    def get_bag(self) -> Bag:
        return self._bag

    def buy(self, ticket: Ticket) -> int:
        return self._bag.hold(ticket)
