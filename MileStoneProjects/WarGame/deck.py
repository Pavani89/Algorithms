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

class Deck:
    def __init__(self):
        # Empty list to initiate a new deck of 52 cards
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                # Create a Card Objet
                created_card = Card(suit, rank)

                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

'''
new_deck = Deck()

for card_obj in new_deck.all_cards:
    print(card_obj)    # prints all the different 52 cards in the deck

bottom_card = new_deck.all_cards[-1]
print('---------------')
print(bottom_card)
print('---------------')
'''