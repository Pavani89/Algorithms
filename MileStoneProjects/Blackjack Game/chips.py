'''
   Class to keep track of a Player's starting chips, bets and ongoing winnings. 
'''

class Chips():
    def __init__(self, total = 100):
        self.total = total      # Start of with 100 chips
        self.bet = 0
    
    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet