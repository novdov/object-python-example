from .bag import Bag
from .ticket import Ticket


class Audience:
    def __init__(self, bag: Bag):
        self._bag = bag

    def get_bag(self) -> Bag:
        return self._bag

    def buy(self, ticket: Ticket) -> int:
        if self._bag.has_invitation():
            self._bag.set_ticket(ticket)
            return 0
        self._bag.set_ticket(ticket)
        self._bag.minus_amount(ticket.get_fee())
        return ticket.get_fee()
