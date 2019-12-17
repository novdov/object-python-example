from .audience import Audience
from .ticket_seller import TicketSeller


class Theater:
    def __init__(self, ticket_seller: TicketSeller):
        self._ticket_seller = ticket_seller

    def enter(self, audience: Audience) -> None:
        """
        관람객을 극장에 입장 시키는 메서드 (관람객이 가질 수 있는 것: 현금, 티켓, 초대장)
            - 관람객이 초대장을 가지고 있을 경우, 티켓을 관람객의 가방에 넣음
            - 관람객이 초대장을 가지고 있지 않을 경우, 관람객의 가방에서 티켓 금액만큼 차감한 후 매표소에 금액을 증가.
              마지막으로 관람객의 가방에 티켓을 넣음

        문제점
            1. 관람객 (`Audience`)과 판매원 (`TicketSeller`)이 극장의 통제를 받는 수동적인 존재임
            2. **`Audience`와 `TicketSeller`를 변경할 경우 `Theater`도 함께 변경해야 함**
               = 변경에 취약한 코드

        - 코드를 이해하기 어렵게 만드는 것
            1. 일반적인 상식과 다르게 동작하는 코드 (극장이 모든 것을 통제함)
            2. 아래 코드의 이해를 위해 여러가지 세부 내용들을 모두 기억하고 있어야 함
        """
        if audience.get_bag().has_invitation():
            ticket = self._ticket_seller.get_ticket_office().get_ticket()
            audience.get_bag().set_ticket(ticket)
        else:
            ticket = self._ticket_seller.get_ticket_office().get_ticket()
            audience.get_bag().minus_amount(ticket.get_fee())
            self._ticket_seller.get_ticket_office().plus_amount(ticket.get_fee())
            audience.get_bag().set_ticket(ticket)
