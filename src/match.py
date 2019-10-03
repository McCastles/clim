
from .player import Player

def start_match(decks, ai=False):
    print('Match started{}!'.format(' vs AI opponent' if ai else ' (hotseat)'))
    print(decks)

    # TODO: nickname input
    naruto = Player(decks[0])
    print(naruto.library)

    naruto.draw()
    print(naruto)



