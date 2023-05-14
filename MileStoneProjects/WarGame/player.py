# from deck import Deck

'''
    1. Hold current list of player cards
    2. Player should be able to add or remove cards from their "hand"
     (list of card object)
    3. We want the player ot be able to add a single or multiple cards to their
        list in one method call.
    4. Translate a Deck/Hand of cards with top and bottom, to a python list
'''

class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)     # Consider left of the array as top of the deck. Hence always remove from top/left of the deck/list

    def add_cards(self, new_cards):  # new_cards coild be a single or multiple cards
        if type(new_cards) == type([]):
            # List if multiple Card objects
            self.all_cards.extend(new_cards)
        else:
            # For a single Card object
            self.all_cards.append(new_cards)

    def __str__(self):
        return  f'Player {self.name} has {len(self.all_cards)} cards'

'''
new_player = Player("Pavani")
print(new_player)

new_deck = Deck()
new_deck.shuffle()
mycard = new_deck.deal_one()

print(mycard)

new_player.add_cards(mycard)
print(new_player)
new_player.add_cards([mycard,mycard])
print(new_player)
'''