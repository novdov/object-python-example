from typing import List

from .ticket import Ticket


class TicketOffice:
    def __init__(self, amount: int, tickets: List[Ticket]):
        self._amount = amount
        self._tickets = tickets

    def get_ticket(self) -> Ticket:
        return self._tickets.pop(0)

    def minus_amount(self, amount: int) -> None:
        self._amount -= amount

    def plus_amount(self, amount: int) -> None:
        self._amount += amount
