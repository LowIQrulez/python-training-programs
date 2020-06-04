# IMPORT STATEMENTS AND VARIABLE DECLARATIONS:

import random
from IPython.display import clear_output


deckdict = {"2 of Hearts":2,"3 of Hearts":3,"4 of Hearts":4,"5 of Hearts":5,"6 of Hearts":6,"7 of Hearts":7,"8 of Hearts":8,"9 of Hearts":9,"10 of Hearts":10,"Jack of Hearts":10,"Queen of Hearts":10,"King of Hearts":10,"Ace of Hearts":11,"2 of Diamonds":2,"3 of Diamonds":3,"4 of Diamonds":4,"5 of Diamonds":5,"6 of Diamonds":6,"7 of Diamonds":7,"8 of Diamonds":8,"9 of Diamonds":9,"10 of Diamonds":10,"Jack of Diamonds":10,"Queen of Diamonds":10,"King of Diamonds":10,"Ace of Diamonds":11,"2 of Spades":2,"3 of Spades":3,"4 of Spades":4,"5 of Spades":5,"6 of Spades":6,"7 of Spades":7,"8 of Spades":8,"9 of Spades":9,"10 of Spades":10,"Jack of Spades":10,"Queen of Spades":10,"King of Spades":10,"Ace of Spades":11,"2 of Clubs":2,"3 of Clubs":3,"4 of Clubs":4,"5 of Clubs":5,"6 of Clubs":6,"7 of Clubs":7,"8 of Clubs":8,"9 of Clubs":9,"10 of Clubs":10,"Jack of Clubs":10,"Queen of Clubs":10,"King of Clubs":10,"Ace of Clubs":11}

playing = True

# CARDS HANDLING SET UP:

class Deck ():
    
    def __init__(self):
        self.deck = list (deckdict.keys())
                             
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand ():
    
    def __init__(self):
        self.hand = []
        self.value = 0   
        self.aces = 0
    
    def add_card(self,card):
        self.hand.append (card)
        self.value = self.value + deckdict[card]
        if card == "Ace of Hearts" or card == "Ace of Diamonds" or card == "Ace of Spaded" or card == "Ace of Clubs":
            self.aces = self.aces + 1
    
    def adjust_for_ace(self):
        if self.value > 21 and self.aces > 0:
            self.value = self.value - 10
            self.aces = self.aces - 1
            
# Hit and stand mechanisms

def hit (deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()
    
def hit_or_stand ():
    while True:
        x = input("Do you want to hit or stand (h/s)?")
        if x.lower() [0] == "h":
            return "h"
        elif x.lower() [0] == "s":
            break
        else:
            print ("Sorry your input is wrong!")

# Betting system set-up
class Bank ():
    
    def __init__ (self,chips=100):
        self.chips = chips
        
    def __str__(self):
        return f"You have {self.chips}"   
    
    def win (self,bet):
        self.chips = self.chips + bet
        
    def lose (self,bet):
        self.chips = self.chips - bet
        
def f_bet ():
    while True:
        try:
            bet = int(input(f"Please place your bet."))
            return bet
        except:
            print ("Sorry, the bet must be a whole number!")
        else:
            if bet > bank.chips:
                print (f"Sorry. You bet more than you got ({player_bank})")
            else:
                break

# CARDS SHOWING MECHANISMS

def show_some (player_hand,dealer_hand):
    print ("Player's hand:")
    for card in player_hand.hand:
        print (card)
    print ("Dealer's hand:")
    for n,card in enumerate (dealer_hand.hand):
        if n == 0:
            print (card)
        else:
            print ("Hidden")
    print ("")

def show_all(player,dealer):
    
    print ("Player's hand:")
    for card in player_hand.hand:
        print (card)
    print(f"Player's Hand = {player.value}")
    
    print ("Dealer's hand:")
    for card in dealer_hand.hand:
        print (card)
    print(f"Dealer's Hand = {dealer.value}")
    print ("")

while playing == True:
    
    clear_output()
    
    deck = Deck ()
    deck.shuffle ()
    
    player_hand = Hand ()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand ()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    the_bet = f_bet ()
    
    try:
        player_bank = Bank (old_player_bank)
    except:
        player_bank = Bank ()
        
    show_some (player_hand,dealer_hand)
    
    while True:
        if player_hand.value < 21:
            if hit_or_stand () == "h":
                player_hand.add_card(deck.deal())
                player_hand.adjust_for_ace()
                show_some (player_hand,dealer_hand)
            else:
                break
        else:
            break
    
    while True:
        if dealer_hand.value < 17:
            dealer_hand.add_card(deck.deal())
            dealer_hand.adjust_for_ace()
        else:
            break      
    
    show_all(player_hand,dealer_hand)
    if player_hand.value > 21:
        player_bank.lose (the_bet)
        print ("Player busts!")
    elif dealer_hand.value > 21:
        player_bank.win (the_bet)
        print ("Dealer busts!")
    elif dealer_hand.value > player_hand.value:
        player_bank.lose (the_bet)
        print ("Dealer wins!")
    elif player_hand.value > dealer_hand.value:
        player_bank.win (the_bet)
        print ("Player wins!")
    elif player_hand.value == dealer_hand.value:
        print ("Its a tie!")

    print (f"Player's bank is now: {player_bank.chips}")
   
    if player_bank.chips > 0:
        new_game = input ("Do you want to play again Y/N")
        if new_game.lower () [0] == "y":
            playing = True
            old_player_bank = player_bank.chips
            continue
        else:
            break
    else:
        new_game = input ("You lost all chips. Do you want to play again Y/N")
        if new_game.lower () [0] == "y":
            playing = True
            old_player_bank = 100
            continue
        else:
            break