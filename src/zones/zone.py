import random

class Zone:

    def __init__(self, owner):
        self.owner = owner
        self.cards = []
        self.zone_name = self.__class__.__name__

    def __repr__(self):
        return f'< Zone: {self.zone_name}. Number of cards: {len(self.cards)} >'

    def shuffle(self):
        random.shuffle(self.cards)
        print(f'{self.owner} shuffles their {self.zone_name}.')

    def gain_cards(self, other_zone, key, qty=1):
        for i in range(qty):
            self.cards.append(key())

    def __len__(self):
        return len(self.cards)