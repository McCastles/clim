
from .zone import Zone

class Library(Zone):

    def __init__(self, cards, owner):

        super().__init__(owner)
        for card in cards:
            self.cards.append(card)
        self.shuffle()

    def display(self, sorted_by='convertedManaCost'):
        super().display(sorted_by=sorted_by)
        self.shuffle()
