''' Program recreating the classic tic-tac-toe game between two players.
    User has to input the coordinates where they wish to place there mark.
    Coordinates starts at [0,0].
    Game continues as long as there is a winner or the user type 'quit' to exit
    Author: Soumya Narayanan '''


import copy
a = []
b = []
player = 1


def build_board(num, size):
    # Building the board:
    for i in range(0, size):
        print(' ---' * size)
        new_row = ""
        for j in range(0, size):
            new_row += str(num[i][j])
        print("| " + " | ".join(new_row) + " | ")
    print(' ---' * size)


def line_check(b, size):
    for i in range(0, size):
        set_r = set(b[i])
        if len(set_r) == 1 and b[i][0] != 0:
            return b[i][0]
    return 0


def diagonal_winner(b, size):
    diag = []
    for i in range(0, size):
        diag.append(b[i][i])
    set_d = set(diag)
    if len(set_d) == 1 and b[0][0] != 0:
        return b[0][0]
    else:
        return 0


def player_switch(cur_player):
    if cur_player == 1:
        cur_player = 2
    else:
        cur_player = 1
    return cur_player


# Getting the user input for the size of the board
size = int(input('Please enter the size of the board: '))
for i in range(0, size):
    a = []
    for j in range(0, size):
        a.append(0)
    b.append(a)

# Printing the initial board
build_board(b, size)

# Starting the game and continue as long as there is a winner or the user wist to:
while True:

    # Getting the coordinates from the user
    coordinates = [int(n, 10) for n in input('Enter the row and column separated by comma: ').split(",")]
    row_num = coordinates[0]
    col_num = coordinates[1]

    if b[row_num][col_num] == 0:
        # Assigning player value to the coordinates user selected and printing the board
        b[row_num][col_num] = player
        build_board(b, size)

        # Check if there is a winner in any of the rows of the board:
        winner_row = line_check(b, size)
        if winner_row > 0:
            print('Congrats!! Winner is: ', player)
            break

        # Transposing the list to check for column wise winner:
        c = [list(i) for i in zip(*b)]
        winner_col = line_check(c, size)
        if winner_col > 0:
            print('Congrats!! Winner is: ', player)
            break

        # checking for the winner diagonally
        winner_diag = diagonal_winner(b, size)
        if winner_diag > 0:
            print('Congrats!! Winner is: ', player)
            break

        # check for the winner in the opposite diagonal
        rev = []
        copy_b = copy.deepcopy(b)
        for i in range(0, size):
            copy_b[i].reverse()
            rev.append(copy_b[i])
        winner_rev_diag = diagonal_winner(rev, size)
        if winner_rev_diag > 0:
            print('Congrats!! Winner is: ', player)
            break

        # Switching the turn to the next player
        player = player_switch(player)

    else:
        print('There is already an entry in that place.. ')

    # Check with user if they want to continue with the game:
    continue_game = input('Type quit to quit!!').lower()
    if continue_game == 'quit':
        break











