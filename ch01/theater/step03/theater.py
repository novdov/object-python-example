from .audience import Audience
from .ticket_seller import TicketSeller


class Theater:
    def __init__(self, ticket_seller: TicketSeller):
        self._ticket_seller = ticket_seller

    def enter(self, audience: Audience) -> None:
        """
        step01 에서 처리하던 부분을 `TicketSeller` 로 이등: 캡술화
        캡슐화를 통해 객체 내부로의 접근을 제한해 객체 간의 결합도를 낮춤
        """
        self._ticket_seller.sell_to(audience)
