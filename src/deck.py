from .card import Card

class Deck:

    def __init__(self, json_deck=None, path=None):
        self.cards = self.parse_decklist(json_deck.get('mainBoard'))
        self.path = path
        self.name = json_deck.get('name')
        print(f'Deck "{self.name}" loaded from {self.path}. It contains {len(self.cards)} cards.')

    def __repr__(self):
        return f'<Deck object: {self.name}>'

    def parse_decklist(self, json_deck):
        cards = []
        for json_card in json_deck:
            original_card = Card(json_card)
            for i in range(original_card.count):
                clone_card = Card(original_card.__dict__)
                cards.append(clone_card)
        return cards
