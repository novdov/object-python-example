from .ticket_office import TicketOffice


class TicketSeller:
    def __init__(self, ticket_office: TicketOffice):
        self._ticket_office = ticket_office

    def get_ticket_office(self) -> TicketOffice:
        return self._ticket_office
