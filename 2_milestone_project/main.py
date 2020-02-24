import classes as cl
import os

def clear():
    '''
    input - no
    output - 0
    cleans the terminal
    '''
    os.system( 'clear' )
    return 0

def end_of_game():
    '''
    input - keyboard
    output - wants to continue False, dont want True
    '''
    while True:
        try:
            anwser = str(input("Do you want to continue [y/n]: "))
        except:
            print("Please provide yes or no anwser [y/n]")
        else:
            if len(anwser) >= 1:
                if anwser[0].lower() == 'y':
                    return False
                elif anwser[0].lower() == 'n':
                    return True
                else:
                    print("Please provide yes or no anwser [y/n]")
            else:
                print("Please provide yes or no anwser [y/n]")
            

def game_continue():
    '''
    input - no
    output - no
    gives opportunity to get the player ready
    '''
    input("Press ENTER button to start game ")

def game():
    clear()
    print("Hello Player!")
    print("Welcome to blacjack!")
    
    player = cl.Player()
    computer = cl.Computer()
    deck = cl.Deck()
    board = cl.Board()

    
    while True:
        #new game
        player.new_game()
        computer.new_game()

        #Player give a bet
        print(f"Your credits equals {player.money}$")
        board.bet = player.bet()
        game_continue()
        clear()
        deck.shuffle()
        
        #Players takes cards
        for i in range(0,2):
            player.take_card(deck.pop_card())
            computer.take_card(deck.pop_card())

        #lambda expressions
        value_player = lambda : deck.player_value(player.hand)
        value_computer_one = lambda : deck.player_value([computer.hand[0]])
        value_computer = lambda : deck.player_value(computer.hand)

        board_print_one_card = lambda : board.table_one_card(player.hand, value_player(), computer.hand, value_computer_one())
        board_print_all_cards = lambda : board.table_all_card(player.hand, value_player(), computer.hand, value_computer())


        #Printing first board
        board_print_one_card()

        #True if BUST
        bust = lambda a : board.do_bust(deck.player_value(a))

        #Hit or Stand while not BUST or Stand
        while not bust(player.hand) and player.hit_or_stand() :
            player.take_card(deck.pop_card())
            board_print_one_card()

        #Computer takes cards if player not bust and has less points than player
        if not bust(player.hand):
            while value_computer() < value_player():
                computer.take_card(deck.pop_card())
        
        board_print_all_cards()

        #checking who win
        if bust(player.hand):
            print("Player BUST")
            print("Computer WINS")
        elif bust(computer.hand):
            print("Computer BUST")
            print("Player WINS")
            player.money += 2*board.bet
        elif value_player() > value_computer():
            print("Player WINS")
            player.money += 2*board.bet
        elif value_player() == value_computer():
            print("DRAW")
            player.money += board.bet
        else:
            print("Computer WINS")

        #does player have any money?
        if player.money == 0:
            print("You are out of cash!")

        #pleyer out of money or wants to end the game
        if  player.money == 0 or end_of_game():
            print("Thank you for game!")
            if player.money != 0:
                print(f"Your credits equals {player.money}$")
            break
        else:
            clear()

#starting game
game()

