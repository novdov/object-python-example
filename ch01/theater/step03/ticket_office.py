from typing import List

from .audience import Audience
from .ticket import Ticket


class TicketOffice:
    def __init__(self, amount: int, tickets: List[Ticket]):
        self._amount = amount
        self._tickets = tickets

    def sell_ticket_to(self, audience: Audience) -> None:
        self.plus_amount(audience.buy(self.get_ticket()))

    def get_ticket(self) -> Ticket:
        return self._tickets.pop(0)

    def minus_amount(self, amount: int) -> None:
        self._amount -= amount

    def plus_amount(self, amount: int) -> None:
        self._amount += amount
