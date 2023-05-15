import random
from cardConstants import suits, ranks
from card import Card

'''
    1. Instantiate a new deck
        Create all 52 card deck
        Hold list of Card objects
    2. shuffle a deck 
        using random library
    3. Deal cards from the deck object
        pop method from card list
'''

class Deck():
    def __init__(self):
        # Empty list to initiate a new deck of 52 cards
        self.deck = []
        for suit in suits:
            for rank in ranks:
                # Create a Card Objet
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'The deck has:  '+  deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card        

'''
new_deck = Deck()
new_deck.shuffle()
print(new_deck)
'''