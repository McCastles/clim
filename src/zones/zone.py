import random


class Zone:

    def __init__(self, owner):
        self.owner = owner
        self.cards = []
        self.zone_name = self.__class__.__name__

    def __repr__(self):
        cards = ''
        for card in self.cards:
            cards += f'{card}\n'
        return f"\n{self.owner}'s {self.zone_name}. Number of cards: {len(self.cards)}\n{cards}"

    def __len__(self):
        return len(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)
        print(f'{self.owner} shuffles their {self.zone_name}.')

    def gain_cards(self, other_zone, key=None, qty=1):
        if not key:
            key = other_zone.get_top
        for i in range(qty):
            self.cards.append(key())

    def display(self, sorted_by='convertedManaCost'):
        self.cards.sort(key=lambda card: getattr(card, sorted_by))
        print(self)

    def get_top(self):
        return self.cards.pop(0)
