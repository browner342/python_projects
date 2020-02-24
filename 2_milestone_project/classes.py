import random
import os

class Deck():
    def __init__(self):
        self.cards = []
        self.suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
        self.ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
        self.values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}
    
    def shuffle(self):
        '''
        input - no
        output - random.shuffle(self.cards)
        shuffle the cards
        '''
        self.cards = []

        for ranks in self.ranks:
            for suits in self.suits:
                self.cards.append(ranks +" "+ suits)

        return random.shuffle(self.cards)

    def pop_card(self):
        '''
        input - no
        output - self.cards.pop()
        '''
        return self.cards.pop()

    def player_value(self, cards):
        '''
        input - list of cards in hand
        output - points 
        '''
        points = 0
        ace = False

        for card in cards:
            #if ace
            if card.split()[0] == 'Ace':
                ace = True

            points += self.values[card.split()[0]]
                    
        if ace == True and points > 21:
            ace = False
            points -= 10
                   
        return points

class Player():
    def __init__(self, money = 100):
        self.money = money
        self.hand = []
        self.points = 0

    def new_game(self):
        '''
        input - no
        output - no
        '''
        self.hand = []
        self.points = 0

    def bet(self):
        '''
        input - keyboard int
        output - int(amout of bet)
        player gives a bet
        '''
        amount = -1
        while True:
            try:
                while amount <= 0 or self.money - amount < 0:
                    amount = int(input("Provide a bet: "))
            except:
                print("It's not a number")
            else:
                self.money -= amount
                break
        
        print(f"Present credits: {self.money}")
        return amount

    def prize(self, amount):
        '''
        input - no
        output - self.money
        '''
        self.money += amount
        return self.money

    def hit_or_stand(self):
        '''
        output - True if Hit or False if Stand
        taking anwser from player
        '''
        while True:
            try:
                anwser = str(input("Hit or Stand: "))
            except:
                print("That's not a hit or stand, provide your anwser again.")
            else:
                if len(anwser) >= 1:
                    if anwser[0].lower() == 'h' or anwser[0].lower() == 's':
                        break
                    else:
                        print("That's not a hit or stand, provide your anwser again.")
                else:
                    print("That's not a hit or stand, provide your anwser again.")

        if anwser[0].lower() == 'h':
            return True
        else:
            return False        

    def take_card(self, card):
        '''
        input - str name of card
        take card to hand
        ''' 
        self.hand.append(card)


class Computer():
    def __init__(self):
        self.hand = []
        self.points = 0

    def new_game(self):
        self.hand = []
        self.points = 0

    def take_card(self, card):
        '''
        input - str name of card
        take card to hand
        ''' 
        self.hand.append(card)

class Board():
    def __init__(self):
        self.score = [0,0]
        self.bet = 0

    def new_game(self):
        self.bet = 0

    def do_bust(self,points):
        '''
        input - points
        output - if points over 21 True else False
        '''
        if points > 21:
            return True
        else:
            return False

    def table_one_card(self, player_hand, player_value, computer_hand, computer_value):
        '''
        input - player_hand, player_value, computer_hand, computer_value
        output - no
        print a table when player could see only one computer's cards
        '''
        os.system( 'clear' )
        print('************************************************************')
        print(f'  {computer_hand[0]}, ###############')
        print('')
        print(f'  Value: {computer_value}')
        print('------------------------------------------------------------')
        print(f'  Value: {player_value}')
        print('')
        print(f'  {player_hand}')
        print('************************************************************')

    def table_all_card(self, player_hand, player_value, computer_hand, computer_value):
        '''
        input - player_hand, player_value, computer_hand, computer_value
        output - no
        print a table when player could see all computer's cards
        '''
        os.system( 'clear' )
        print('************************************************************')
        print(f'  {computer_hand}')
        print('')
        print(f'  Value: {computer_value}')
        print('------------------------------------------------------------')
        print(f'  Value: {player_value}')
        print('')
        print(f'  {player_hand}')
        print('************************************************************')


if __name__ == '__main__':
    pass