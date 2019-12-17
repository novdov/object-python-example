from .bag import Bag


class Audience:
    def __init__(self, bag: Bag):
        self._bag = bag

    def get_bag(self) -> Bag:
        return self._bag
