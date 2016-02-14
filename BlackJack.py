# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 20:03:16 2016

@author: yuvaraj
"""

import random,sys
suits = {'club':1,'diamonds' : 1,'spade' : 1,'hearts' : 1}
cards = {'ace':11,'one':1,'two':2,'three': 3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten': 10,'king':10,'queen':10,'jack':10}

class Pack(object):
    def __init__(self,suits,cards):
        self.suits = suits
        self.cards = cards
        
    def my_deck(self,suits,cards):
        my_deck1 = []
        for i in self.suits:
            for j in self.cards:
                my_deck1.append(i+"_"+j)
        return my_deck1
# defining main here:
def main():   
  
#    print shoe
# Declaring of methods start from here:    
# Declaring method for showing players cards:    
    def PlayersHand(shoe):
        print "Your Cards are:"
        r = []
        for i in range(2):
            l = random.choice(shoe)
            r.append(l)
        return r 
 # Declaring method to show dealers hand:       
    def dealersHand(shoe):
        print "dealer is having the card :%s" %random.choice(shoe)
        dealer_cards = []
        dealer_cards.append(random.choice(shoe))
        return dealer_cards
# Declaring method to calculate sum of cards
    def sum_of_cards(now_cards):
        sum = 0
        for l in now_cards:
            a,b = l.split('_')
            sum = sum + cards.get(b)
        return sum 
    def propmt_for_users_choice():
        players_choice = raw_input("Please enter if you want to Stand/Hit ?? ")
        return players_choice
# The flow starts here:
    my_pack = Pack(suits,cards)
    shoe = []
    shoe = my_pack.my_deck(suits,cards) 
    player_amount = raw_input ("Please Enter the amount You have in total:")
    player_amount = int(player_amount)
    player_bet_amount = raw_input("what's your bet:")
    player_bet_amount = int(player_bet_amount)
    if player_amount > player_bet_amount:
        players_hand = PlayersHand(shoe)
        print players_hand
        print "the sum of your cards now is:",sum_of_cards(players_hand) 
        dealers_hand = dealersHand(shoe)
        print dealers_hand
    else:
        print "you dont have enough to bet"
        sys.exit(0)
    players_choice = raw_input("Please enter if you want to Stand/Hit ?? ")
    if player_amount > player_bet_amount:
        while(players_choice.lower() == 'hit' or players_choice.lower() == 'stand' ):
            if player_amount > player_bet_amount:
                if players_choice.lower() == 'hit':
                    r = random.choice(shoe)
                    players_hand.append(r)      
                    print "your cards now are:",players_hand
                    sum_now_player = sum_of_cards(players_hand)
                    print "The sum of your cards now:",sum_now_player 
                    if sum_now_player > 21:
                        print ("you are bust out of the game as your score:%s,is greater than 21"%sum_now_player)
                        player_amount = (player_amount) - (player_bet_amount)
                        print "you amount now is:",player_amount
                        sys.exit(0)
                    elif sum_now_player == 21:
                        print "now your sum is 21, you better stand!!!"
        #                players_choice = raw_input( "enter your choice now, you gonna stand or hit??")
                        players_choice = propmt_for_users_choice()
    #                    continue 
                        continue
                    else:
                        players_choice = propmt_for_users_choice()
                        continue
                elif players_choice.lower() == 'stand':
                    dh2 = random.choice(shoe)
                    dealers_hand.append(dh2)
                    sum_now_dealer = sum_of_cards(dealers_hand)
                    sum_now_player = sum_of_cards(players_hand)
                    print ("The dealers hand is now having cards:%s with sum:%s" %(dealers_hand,sum_now_dealer))
                    if sum_now_player > sum_now_dealer:
                        player_amount = player_amount + player_bet_amount
                        print "you won the pot!!!, and your amount is now:",player_amount
                        sys.exit(0)
                    elif sum_now_player < sum_now_dealer:
                        player_amount = player_amount - player_bet_amount
                        print "you lost the pot!!!, and your amount is now:",player_amount
                        sys.exit(0)
                    elif sum_now_player == sum_now_dealer:
                        print "its a Push,you neither gained nor lost, your amount now is:",player_amount
                        sys.exit(0)
                else:
                    print"Sorry you dont have the bet amount"
                    sys.exit(0)
    else:
        print"Sorry you dont have the bet amount"
        sys.exit(0)                
            
            
#        else:
#            players_choice = raw_input("Please enter a valid choice: Stand/Hit ?? ") 
# Calling main here:        
if __name__ == "__main__": main()  