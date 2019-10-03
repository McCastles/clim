# from .engine import engine

class Card:

    def __init__(self, json_data):
        
        self.__dict__.update(json_data)
        
        # print(f'{self.count} copies of {self.name} added to the deck.')
        # print(self)

    # TODO: repr
    def __repr__(self):
        return f'<id: {id(self)} Card object; Name: {self.name}; Colors: {self.colors}; etc.>'