
import sys
from .player import Player
from .turn import Turn


def start_match(decks, ai=False):
    print('\nMatch started{}!'.format(' vs AI opponent' if ai else ' (hotseat)'))

    # player1 = Player(decks[0], input('\nPlayer 1 name >>> '))
    # player2 = Player(decks[1], input('\nPlayer 2 name >>> '))

    players = (Player(decks[0]), Player(decks[1], 'Sasuke'))
    
    # TODO: Mulligan Loop
    for player in players:
        keep = False
        input(f'\n{player.name}, get ready to draw your opening hand. [press any key]')
        player.draw(7)
        while not keep:
            player.hand.display()
            response = input(f'{player.name} keeps? (yes/no) >>> ')
            if len(player.hand) == 1 or response == 'yes' or response == '':
                keep = True
            else:
                player.mulligan()
    

    turn = Turn()
    while True:
        input(f'Turn {turn.no} begins! [press any key]')
        turn.no = turn.no + 1
        for player in players:
            if not turn.make_turn(players, player.name):
                sys.exit('Game over!')

