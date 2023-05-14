# import cardConstants as CC
from cardConstants import values

'''
    Card class to define the suit, rank and its value
'''
class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        #self.value = CC.values[rank]
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + " of "  + self.suit
    
'''
new_card = Card('Diamonds', 'Three')
print(new_card)
print(new_card.value)
'''