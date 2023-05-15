from cardConstants import suits, ranks, values
from deck import Deck
from card import Card
from hand import Hand
from chips import Chips

'''
    Add some functionality to the game
    1. take the bet and check if the player can wager that many chips
    2. taking hits: taking deck and hand as input, and deal one card off and add it 
    to Hand, check for aces if the player's hand exceeds 21
    3. Prompt player to hit or stand
    4. show one of dealer's card, and player's card(2). At the end, all cards are shown
    5. Handle end of the game scenarios - pass player's hand, dealer's hand and chips as needed
'''
playing = True

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except ValueError:
            print("Sorry please enter a number")
        else:
            if chips.bet > chips.total:
                print(f"Sorry, you do not have enough chips! You have: {chips.total}")
            else:
                break


def hit(deck, hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input("Hit or Stand? Enter h or s ")
        
        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print("Player stands, Dealer's Turn")
            playing = False
        else:
            print("Sorry, input not valid, please enter h or s only!")
            continue
        break

def show_some(player, dealer):
    # Show only ONE of the Dealer's cards
    print("\n Dealer's Hand: ")
    print("First card hidden!")
    print(dealer.cards[1])

    # Show all (2 cards) of the Player's hand/cards
    print("\n Player's Hand: ")
    for card in player.cards:
        print(card)

    
def show_all(player, dealer):
    # show all the dealer's cards
    print("\n Dealer's Hand: ")
    for card in dealer.cards:
        print(card)               
    '''
        An alternate way to print all values instead of looping
            # show all the dealer's cards
            print("\n Dealer's Hand: ", *dealer.cards, sep='\n')
    '''
    # calculate and display value
    print(f"Value of Dealer's hand is: {dealer.value}")

    # Show all (2 cards) of the Player's hand/cards
    print("\n Player's Hand: ")
    for card in player.cards:
        print(card)
    # calculate and display value
    print(f"Value of Player's hand is: {player.value}")

# End Game Scenaios
def player_busts(player, dealer, chips):
    print("BUST Player!")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("Player WINS!")
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print("Dealer BUST, PLayer WINS!")
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print("Dealer WINS!")
    chips.lose_bet()

def push(player, dealer):
    print("Dealer and Player tie! PUSH")


# GAME LOGIC
while True:

    # Print an opening statement
    print("Welcome to BLACKJACK!!!")
    deck = Deck()
    deck.shuffle()

    # set up the player and dealer cards
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Set up the Player's chips
    player_chips = Chips()

    # Prompt the Player for their bet
    take_bet(player_chips)

    # Show Cards (2 of players card, one from dealer)
    show_some(player_hand, dealer_hand)

    # Play
    playing = True
    while playing:
        # Prompt for Player tp Hit or Stand
        hit_or_stand(deck, player_hand)

        # Show cards (2 of players card, one from dealer)
        show_some(player_hand, dealer_hand)

        # If player's hand exceeds 21, run player_bust() and break out of the loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            playing=False
            break

    # If player hasn't busted, play Dealer's hand until Dealer reaches Player's value
    if player_hand.value <= 21:

        while dealer_hand.value < player_hand.value:
            hit(deck, dealer_hand)

            # Show all cards
            show_some(player_hand, dealer_hand)

            # Run different winning scenarios
            if dealer_hand.value > 21:
                dealer_busts(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand, player_chips)
            else:
                push(player_hand, dealer_hand)
    
    # Inform Player of their chips total
    print(f"\n Player total chips are at: {player_chips.total}")
    # Ask to play again
    new_game = input("Would you like another game? y/n: ")

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thank You for Playing!")
        break