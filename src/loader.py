
import glob
import json
import os
import sys

from .deck import Deck
from .match import start_match


def format_deck(name_deck):
    return f'{os.path.splitext(os.path.basename(name_deck))[0]}'


def load(argv):
    avail_decks = [f for f in glob.glob('decks/*.json')]

    if (not argv or any(cmd in argv for cmd in ['help', 'decks'])):
        print('Usage: python3 clim green\nAvailible decks:')
        for name in avail_decks:
            print(format_deck(name))
        sys.exit()

    chosen_decks = [f'decks/{deckname}.json' for deckname in argv]

    decks = []

    for deck_path in chosen_decks:
        if os.path.exists(deck_path) and os.path.isfile(deck_path):
            f = open(deck_path, 'r')
            deck_obj = Deck(json.load(f), deck_path)
            decks.append(deck_obj)
            f.close()
        else:
            print(f'Oops! Deck {format_deck(deck_path)} not found')
            sys.exit()

    # print(' vs. '.join([format_deck(name) for name in chosen_decks]))

    # mode = input('Play mode:\n1. Hotseat\n2. AI\n>>> ')
    # if mode == '2':
        # start_match(decks, ai=True)
    # else:
    start_match(decks)
