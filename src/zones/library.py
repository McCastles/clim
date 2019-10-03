
from .zone import Zone

class Library(Zone):

    def __init__(self, cards, owner):

        super().__init__(owner)
        for card in cards:
            self.cards.append(card)
        self.shuffle()

    def pop(self):

        return self.cards.pop()
