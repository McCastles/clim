
from .player import Player


def start_match(decks, ai=False):
    print('\nMatch started{}!'.format(' vs AI opponent' if ai else ' (hotseat)'))

    # TODO: nickname input
    # player1 = Player(decks[0], input('\nPlayer 1 name >>> '))
    # player2 = Player(decks[1], input('\nPlayer 2 name >>> '))

    player1 = Player(decks[0])
    player2 = Player(decks[1], 'Sasuke')
    
    # TODO: Mulligan Loop
    for player in (player1, player2):
        player.draw(7)
        keep = False
        input(f'\n{player.name} get ready to draw your opening hand. [press any key]')
        while not keep:
            player.hand.display()
            response = input(f'{player.name} keeps? (yes/no) >>> ')
            if len(player.hand) == 1 or response == 'yes' or response == '':
                keep = True
            else:
                player.mulligan()
