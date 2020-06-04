#clear output function import

from IPython.display import clear_output

# Displaying of the game board

def display_board(board):
    clear_output ()
    print ("-------------")
    print ("| " + board [7] + " | " + board [8] + " | " + board [9] + " |")
    print ("-------------")
    print ("| " + board [4] + " | " + board [5] + " | " + board [6] + " |")
    print ("-------------")
    print ("| " + board [1] + " | " + board [2] + " | " + board [3] + " |")
    print ("-------------")
    
    
#Player one chooses marker and player two gets opposite marker

def player_input():
    marker = ""
    while marker != "X" and marker != "O":
        marker = input ("Player 1, choose your marker X/O!").upper ()
    player1 = marker
    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"
    return (player1,player2)


#Function defining where to place a marker on board.

def place_marker(board,marker,position):
    board [position] = marker

    
#A function checking if chosed place on board is empty.

def space_check(board, position):
    if board [position] == " ":
        return True
    else:
        return False
    
    
# A function checking if the board isnt full and so there is a tie.    
    
def full_board_check(board):
    if " " not in board [1:11:1]:
        return True
    else:
        return False
    
#A function defining which player goes first.   

import random
def choose_first():
    if random.randint (1,2) == 1:
        return ("Player 1")
    else:
        return ("Player 2")

#Function checking if the specific marker didnt reach a victory conditions

def win_check(board, marker):
    if board [1:4:1] == [marker,marker,marker]:
        return True
    elif board [4:7:1] == [marker,marker,marker]:
        return True
    elif board [7:10:1] == [marker,marker,marker]:
        return True
    elif board [2:9:3] == [marker,marker,marker]:
        return True
    elif board [3:10:3] == [marker,marker,marker]:
        return True
    elif board [1:10:4] == [marker,marker,marker]:
        return True
    elif board [3:8:2] == [marker,marker,marker]:
        return True
    elif board [1:8:3] == [marker,marker,marker]:
        return True
    else:
        return False

#Function taking input of players, a number, defining where the marker should be placed.
    
def player_choice(board):
    position = 0
    while position not in (1,2,3,4,5,6,7,8,9) or space_check(board,position) == False:
        position = int (input ("Where (1-9) you want to place your marker?"))
    return position

#Function asking a players if to continue with another game.

def replay():
    if input ("Play again? Y/N.") == "Y":
        return True
    else:
        return False

#actuall game
print ("Welcome to Tic Tac Toe game!")

while True:

    board = [" "] * 10

    player1,player2 = player_input()
    print (f"Player's 1 marker is {player1} and player's 2 marker is {player2}!")

    turn = choose_first()
    print (f"{turn} starts!")

    game = input (f"{turn} Can we start? Y/N")
    if game == "Y":
        game_on = True
    else:
        game_on = False

    while game_on == True:

        if turn == "Player 1":
            display_board(board)

            position = player_choice (board)

            place_marker (board,player1,position)

            if win_check(board,player1) == True:
                display_board(board)
                print ("Player 1 won!")
                game_on = False
            else:
                if full_board_check(board) == True:
                    display_board(board)
                    print ("Its a tie")
                    game_on = False
                else:
                    turn = "Player 2"
        elif turn == "Player 2":
            display_board(board)

            position = player_choice (board)

            place_marker (board,player2,position)

            if win_check(board,player2) == True:
                display_board(board)
                print ("Player 2 won!")
                game_on = False
            else:
                if full_board_check(board) == True:
                    display_board(board)
                    print ("Its a tie")
                    game_on = False
                else:
                    turn = "Player 1"
                    
    if replay () != True:
        break
    

