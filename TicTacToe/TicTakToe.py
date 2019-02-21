import random
def display_board(board):
    print("  {}  |  {}  |  {}  ".format(board[7], board[8], board[9]))
    print("------------------")
    print("  {}  |  {}  |  {}  ".format(board[4], board[5], board[6]))
    print("------------------")
    print("  {}  |  {}  |  {}  ".format(board[1], board[2], board[3]))

def player_input(plyr):
    player = {1: '', 2: ''}
    player[plyr] = input("Player {}: Please pick a marker 'X' or 'O'".format(plyr))
    while (player[plyr].upper() not in "XO") or player[plyr] == '':
        print("Please pick a valid marker")
        player[plyr] = input("Player {}: Please pick a marker 'X' or 'O'".format(plyr))
    print("Player {} will go First".format(plyr))
    player[plyr] = player[plyr].upper()
    if player[1].upper() == 'X':
        player[2] = 'O'
    elif player[1].upper() == 'O':
        player[2] = 'X'
    elif player[2].upper() == 'X':
        player[1] = 'O'
    else:
        player[1] = 'X'
    return player
    
def place_marker(board, marker, position):
    board[position] = marker
    return board

def win_check(board, mark):
    if board[1] == board[2] == board[3] == mark:
        return True
    elif board[1] == board[4] == board[7] == mark:
        return True
    elif board[1] == board[5] == board[9] == mark:
        return True
    elif board[7] == board[8] == board[9] == mark:
        return True
    elif board[3] == board[6] == board[9] == mark:
        return True
    elif board[3] == board[5] == board[7] == mark:
        return True
    elif board[2] == board[5] == board[8] == mark:
        return True
    elif board[4] == board[5] == board[6] == mark:
        return True
    else:
        return False

def choose_first():
    return random.randint(1, 2)
    
def space_check(board, position):
    return board[position] == ''
    
def full_board_check(board):
    for i in range(1, len(board)):
        if board[i] == '':
            return False
    else:
        return True

def player_choice(board, plyrno):
    pos = int(input("Player {}: Please provide your next position between 1 - 9".format(plyrno)))
    #display_board(board)
    while pos not in range(1, 10):
        print("Please enter a valid position")
        pos = int(input("Player {}: Please provide your next position between 1 - 9".format(plyrno)))
        #display_board(board)
    if space_check(board, pos) == True:
        return pos
    else:
        print("Position not Free")
        
def replay():
    playagain = input("Do you want to play again: Y or N")
    while playagain.upper() not in 'YN':
        print("Please enter a valid choice")
        playagain = input("Do you want to play again: Y or N")
    return playagain.upper() == 'N'
    
test_board = ['#','','','','','','','','','']
#print(win_check(test_board,'X'))
#place_marker(test_board,'$',8)
#display_board(test_board)
#print(choose_first())
#player_input()
#print(space_check(test_board, 7))
#print(full_board_check(test_board))
#print(player_choice(test_board))
#print(replay())
print('Welcome to Tic Tac Toe!')
while True:
    board = list(test_board)
    #display_board(test_board)
    plyr_no = choose_first()
    plyr_choice = player_input(plyr_no)
    print(plyr_choice)
    print("\n")
    ans = input("Are you Ready to Play: Yes or No")
    while ans not in ['Yes', 'No']:
        print("Please enter a valid option")
        ans = input("Are you Ready to Play: Yes or No")
    if ans == 'Yes':
        print("Let's start")
        game_on = True
        while game_on == True:
            while plyr_no == 1:
                plyr1poschoice = player_choice(board, 1)
                while plyr1poschoice == None:
                    plyr1poschoice = player_choice(board, 1)
                board = place_marker(board,plyr_choice[plyr_no],plyr1poschoice)
                print("\n")
                display_board(board)
                if win_check(board,plyr_choice[plyr_no]) == True:
                    print("Player {} wins the Match".format(plyr_no))
                    game_on = False
                    break
                else:
                    if full_board_check(board) == False:
                        plyr_no = 2
                    else:
                        print("Match is a draw")
                        game_on = False
                        break
                    
            while plyr_no == 2:
                plyr2poschoice = player_choice(board, 2)
                while plyr2poschoice == None:
                    plyr2poschoice = player_choice(board, 2)
                print(plyr2poschoice)
                board = place_marker(board,plyr_choice[plyr_no],plyr2poschoice)
                print("\n")
                display_board(board)
                if win_check(board,plyr_choice[plyr_no]) == True:
                    print("Player {} wins the Match".format(plyr_no))
                    game_on = False
                    break
                else:
                    if full_board_check(board) == False:
                        plyr_no = 1
                    else:
                        print("Match is a draw")
                        game_on = False
                        break
    if replay() == True:
        break
    else:
        continue