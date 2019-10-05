# from .engine import engine

class Card:

    def __init__(self, json_data):
        
        self.__dict__.update(json_data)
        if not hasattr(self, 'manaCost'):
            setattr(self, 'manaCost', '{0}')
        
        # print(f'{self.count} copies of {self.name} added to the deck.')
        # print(self)

    def __len__(self):
        return len(self.manaCost)


    def __repr__(self):
        return f'{self.manaCost} {self.name} ({self.type})'