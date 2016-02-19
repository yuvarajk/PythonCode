# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 20:03:16 2016

@author: yuvaraj
"""

import random,sys
suits = {'club':1,'diamonds' : 1,'spade' : 1,'hearts' : 1}
cards = {'ace':11,'one':1,'two':2,'three': 3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten': 10,'king':10,'queen':10,'jack':10}

class Pack(object):

    def my_deck(self,suits,cards):
        my_deck1 = []
        for i in suits:
            for j in cards:
                my_deck1.append(i+"_"+j)
        return my_deck1


class hand(object):
    def sum_of_hand(self, cards_on_hand):
        sum_hand = 0
        for l in cards_on_hand:
            a,b = str(l).split('_')
            sum_hand = sum_hand + int(cards.get(b))
        return sum_hand
    def spin_cards(self,count):
        shoe = Pack().my_deck(suits, cards)
        r = []
        for i in range(count):
            l = random.choice(shoe)
            r.append(l)
        return r


class choice(object):
    def propmt_for_users_choice(self, option):
        if option == 'new_game':
            players_choice = str(raw_input("Do you want to play one more game: 'yes' or 'no' "))
            return players_choice
        elif option == 'current_game':
            players_choice = str(raw_input("Please enter if you want to Stand/Hit ?? "))
            return players_choice
    def ValidatePlayersChoice(self,players_choice,option):
        if option == 'current_game':
            if players_choice.lower() == 'hit' or players_choice.lower() == 'stand':
                return players_choice
            else:
                print "Please enter a valid choice"
                choice().prompt_for_users_choice(option)
        if option == 'new_game':
            if players_choice.lower() == 'yes' or players_choice.lower() == 'no':
                return players_choice
            else:
                print "Please enter a valid choice"
                choice().prompt_for_users_choice(option)


class gambler(object):
    def get_pocket(self,player_amount,option):
        if option == 'new_game':
            player_amount = int (raw_input("Please Enter the amount You have in total:"))
            return player_amount
        elif option == 'current_game':
            player_amount += player_amount
            return player_amount

    def get_bet(self):
        self.bet_amount = int(raw_input("what's your bet:"))
        return self.bet_amount


class Game():
    def new_game(self,player_amount_carried):
        if player_amount_carried == 0:
            player_amount = gambler().get_pocket(0,'new_game')
            player_bet_amount = gambler().get_bet()
            self.start_game(player_amount,player_bet_amount)

        else:
            player_amount = player_amount_carried
            player_bet_amount = gambler().get_bet()
            self.start_game(player_amount,player_bet_amount)

    def start_game(self, player_amount, player_bet_amount):
        if player_amount >= player_bet_amount:
            players_hand = hand().spin_cards(2)
            print players_hand
            print "the sum of your cards now is:",hand().sum_of_hand(players_hand)
            dealers_hand = hand().spin_cards(1)
            print "dealer's card is:",dealers_hand
            self.current_game(player_amount,player_bet_amount,players_hand,dealers_hand)
        else:
            print "you dont have enough to bet!! exiting the game"
            sys.exit(0)

    def current_game(self,player_amount,player_bet_amount,players_hand,dealers_hand):
        players_choice = choice().propmt_for_users_choice('current_game')
        if player_amount >= player_bet_amount:
            while(str(players_choice).lower() == 'hit' or str(players_choice).lower() == 'stand' ):
                if player_amount >= player_bet_amount:
                    if players_choice.lower() == 'hit':
                        r = []
                        r = hand().spin_cards(1)
                        players_hand.append(r[0])
                        print "your cards now are:",players_hand
                        sum_now_player = hand().sum_of_hand(players_hand)
                        print "The sum of your cards now:",sum_now_player
                        if sum_now_player > 21:
                            print ("you are bust out of the game as your score:%s,is greater than 21"%sum_now_player)
                            player_amount = (player_amount) - (player_bet_amount)
                            print "your amount now is:",player_amount
                            players_choice = choice().propmt_for_users_choice('new_game')
                            choice().ValidatePlayersChoice(players_choice,'new_game')
                            if players_choice == 'yes':
    
                                self.new_game(player_amount)
                            if players_choice == 'no':
                                print "Thanks for playing with us"
                                sys.exit(0)
                            
            
    
                        elif sum_now_player == 21:
                            print "now your sum is 21, you better stand!!!"
                            players_choice = choice().propmt_for_users_choice('current_game')
                            choice().ValidatePlayersChoice(players_choice,'current_game')
                            continue
        
                        else:
                            players_choice = choice().propmt_for_users_choice('current_game')
                            choice().ValidatePlayersChoice(players_choice,'current_game')
                            continue
                    elif players_choice.lower() == 'stand':
                        dh2 = hand().spin_cards(1)
                        dealers_hand.append(dh2[0])
                        sum_now_dealer = hand().sum_of_hand(dealers_hand)
                        sum_now_player = hand().sum_of_hand(players_hand)
                        print ("The dealers hand is now having cards:%s with sum:%s" %(dealers_hand,sum_now_dealer))
                        if sum_now_player > sum_now_dealer:
                            player_amount = player_amount + player_bet_amount
                            print "you won the pot!!!, and your amount is now:",player_amount
                            players_choice = choice().propmt_for_users_choice('new_game')
                            choice().ValidatePlayersChoice(players_choice,'new_game')
                            if players_choice == 'yes':
    
                                self.new_game(player_amount)
                            if players_choice == 'no':
                                print "Thanks for playing with us"
                                sys.exit(0)
 
                        elif sum_now_player < sum_now_dealer:
                            player_amount = player_amount - player_bet_amount
                            print "you lost the pot!!!, and your amount is now:",player_amount
                            players_choice = choice().propmt_for_users_choice(player_amount,'new_game')
                            choice().ValidatePlayersChoice(players_choice,'new_game')
                            if players_choice == 'yes':
                                self.new_game(player_amount)
                            if players_choice == 'no':
                                print "Thanks for playing with us"
                                sys.exit(0)
  
                        elif sum_now_player == sum_now_dealer:
                            print "its a Push,you neither gained nor lost, your amount now is:",player_amount
                            players_choice = choice().propmt_for_users_choice(player_amount,'new_game')
                            choice().ValidatePlayersChoice(players_choice)
                            players_choice = choice().propmt_for_users_choice(player_amount,'new_game')
                            choice().ValidatePlayersChoice(players_choice,'new_game')
                            if players_choice == 'yes':
                                self.new_game(player_amount)
                            if players_choice == 'no':
                                print "Thanks for playing with us"
                                sys.exit(0)
   
                    else:
                        print"Sorry you dont have the bet amount"
                        sys.exit(0)
        else:
            print"Sorry you dont have the bet amount"
            sys.exit(0)


def main():
    Game().new_game(0)

if __name__ == "__main__": main()