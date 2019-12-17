from typing import Optional

from .invitation import Invitation
from .ticket import Ticket


class Bag:
    def __init__(self, invitation: Optional[Invitation] = None, amount: int = 0):
        self._ticket = None
        self._invitation = invitation
        self._amount = amount

    def has_invitation(self) -> bool:
        return self._invitation is not None

    def has_ticket(self) -> bool:
        return self._ticket is not None

    def set_ticket(self, ticket: Ticket) -> None:
        self._ticket = ticket

    def minus_amount(self, amount: int) -> None:
        self._amount -= amount

    def plus_amount(self, amount: int) -> None:
        self._amount += amount
