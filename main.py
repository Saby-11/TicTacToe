# Tic Tac Toe begins
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
game_going= True

winner=None

current_player="X"

def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2] + "|")
    print(board[3] + "|" + board[4] + "|" + board[5] + "|")
    print(board[6] + "|" + board[7] + "|" + board[8] + "|")

def play_game():

    display_board()

    while game_going:
        handle_turn(current_player)

        check_if_game_over()


        flip_player()

#game end
    if winner == "X" or winner == "0":
        print(winner + " won")
    elif winner == "None":
        print("tie")


def handle_turn(player):
    pos = input("choose position from 1 to 9")
    pos = int(pos) - 1
    board[pos]= player
    display_board()

def check_if_game_over():
    check_win()
    check_tie()

def check_win():
    #global variable

    global winner
    row_winner=check_rows()
    col_winner=check_cols()
    diag_winner=check_diags()

    if row_winner:
        winner = row_winner

    elif col_winner:
        winner = col_winner

    elif diag_winner:
        winner=diag_winner

    else:
        winner=None
    return

def check_rows():
    global game_going
    row_1 = board[0] == board[1] == board[2] !="-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        game_going= False
        if row_1:
            return board[0]
        elif row_2:
            return board[3]
        elif row_3:
            return board[6]
    return

def check_cols():
    global game_going
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"
    if col_1 or col_2 or col_3:
        game_going = False
        if col_1:
            return board[0]
        elif col_2:
            return board[1]
        elif col_3:
            return board[2]
    return

def check_diags():
    global game_going
    diag_1 = board[0] == board[4] == board[8] != "-"
    diag_2 = board[6] == board[4] == board[2] != "-"
    if diag_1 or diag_2:
        game_going = False
        if diag_1:
            return board[0]
        elif diag_2:
            return board[6]
    return


def check_tie():
    return

def flip_player():

    global current_player

    if current_player == "X":
        current_player= "0"

    elif current_player == "0":
        current_player= "X"
    return



play_game()

