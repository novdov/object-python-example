class Ticket:
    def __init__(self):
        self._fee = 0

    def get_fee(self):
        return self.fee

    @property
    def fee(self):
        return self._fee
