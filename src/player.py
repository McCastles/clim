
from .zones.library import Library
from .zones.hand import Hand


class Player:

    def __init__(self, deck, name=None):
        if name:
            self.name = name
        else:
            self.name = 'Naruto'
        print(f'Player name set: {self.name}')

        self.library = Library(deck.cards, self.name)
        self.hand = Hand(self.name)

    def __repr__(self):
        return f'''
        Player: {self.name}\n
        Cards in hand:{len(self.hand)}\n
        Cards in library:{len(self.library)}
        '''

    def draw(self, qty=1):
        self.hand.gain_cards(self.library, qty=qty, key=self.library.get_top)
        print(f'{self.name} draws {qty} card(s).')

    def mulligan(self):
        new_size = len(self.hand) - 1
        self.library.gain_cards(self.hand, qty=len(self.hand))
        print(f'Now {self.name} hand is empty: {len(self.hand)} {len(self.library)}')
        self.draw(new_size)
        self.library.shuffle()

