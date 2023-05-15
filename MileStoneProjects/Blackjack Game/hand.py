from cardConstants import suits, ranks, values
from deck import Deck

'''
    Represent the cards help by the player and dealer.
    1. In this class, cards are added to individual players
    2. Values of the cards are pre-calculated
    3. value of Ace is adjusted
'''

class Hand():
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0 # start with zero
        self.aces = 0 # add an attribute to keep track of aces
    
    def add_card(self, card):
        # The card passed will be from Deck class
        # from Deck.deal() --> single Card(suit,rank)
        self.cards.append(card)
        self.value += values[card.rank]

        #track aces
        if card.rank == 'Aces':
            self.aces += 1

    def adjust_for_ace(self):
        # if total value is greater tan 21, change ace to 1 from 11
        while self.aces and self.value > 21:
            self.value -= 10
            self.aces -= 1


'''
test_deck = Deck()
test_deck.shuffle()

test_player = Hand()
pulled_card = test_deck.deal()
print(pulled_card)
test_player.add_card(pulled_card)
print(test_player.value)
'''