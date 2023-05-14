from card import Card
from deck import Deck
from player import Player

'''
    Main logic for the Game
    1. Create a new deck
    2. Split the deck between two players using for loop
    3. Check for 0 cards(though it might not be the case ofr start, but still check), set a bool value; game_on = True
    4. Run a while loop based on game_on status, each player draws cards, run comparision between the cards
    5. Based on the higher value of the card, the player wins those cards and they get added (bottom) to player's list
    6. In case of war, both players have same value card and player need to draw addtional 3 cards. This can be done inside '
        another while at_war (as there could be multiple ties in a row)
    7. Tie ends, check for game_on. if one player has not cards, break the while loop, other player wins.
    
'''

# Game Setup
player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()

# split the 52 cards between the two players
for _ in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True
round_num = 0

# while game_on
while game_on:
    round_num += 1
    print(f"Round '{round_num}'")

    if len(player_one.all_cards) == 0:
        print('Player One, out of cards! Player Two Wins!')
        game_on = False
        break
    if len(player_two.all_cards) == 0:
        print('Player Two, out of cards! Player One Wins!')
        game_on = False
        break
    
    # Start a new round
    player_one_cards = []   # current card in play i.e. card dropped from the player deck
    player_one_cards.append(player_one.remove_one())    #drop from all_cards and add to cards

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    # while at_war
    at_war = True
    while at_war:
        # check if player 1 cards are greater
        if player_one_cards[-1].value > player_two_cards[-1].value:
            # Add the player one deck and player two open deck to player one's deck
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            # Not at war
            at_war = False
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            # Add the player one deck and player two open deck to player one's deck
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            
            # Not at war
            at_war = False
        else:
            print('WAR!')
            if len(player_one.all_cards) < 5:
                print('Player One unable to declare war')
                print("Player TWO WINS!")
                game_on = False
                break 

            elif len(player_two.all_cards) < 5:
                print('Player Two unable to declare war')
                print("Player ONE WINS!")
                game_on = False
                break 
            else:
                for _ in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())


# print(len(player_one.all_cards))
# print(player_one.all_cards[0])