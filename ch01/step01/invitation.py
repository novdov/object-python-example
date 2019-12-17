from datetime import datetime


class Invitation:
    def __init__(self, dt_fmt: str = "%Y-%m-%d"):
        self._when = datetime.now().strftime(dt_fmt)

    @property
    def when(self):
        return self._when
