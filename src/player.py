    
from .zones.library import Library, Zone

class Player:

    def __init__(self, deck, name=None):
        if name:
            self.name = name
        else:
            self.name = 'Naruto'
        print(f'Player name set: {self.name}')

        self.library = Library(deck.cards, self.name)
        self.hand = Zone(self.name)

    def draw(self, qty=1):
        self.hand.gain_cards(self.library, qty=qty, key=self.library.pop)
        print(f'{self.name} draws {qty} card(s).')

    def __repr__(self):
        return f'''
        Player: {self.name}\n
        Cards in hand:{len(self.hand)}\n
        Cards in library:{len(self.library)}
        '''