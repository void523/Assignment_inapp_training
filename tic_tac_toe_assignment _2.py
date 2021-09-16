# Problem Statement
# Create a Tic Tac Toe game.
#
# Here are the requirements:
#
# Two players should be able to play the game (user, computer)
# The board should be printed out every time a player makes a move
# You should be able to accept input of the player position and then place a symbol on the board
# - Store the Game logs (info about the moves, result) for 10 games into a data structure.
# - You should be able to recreate the moves and print out the board for each of the moves for any of the 10 games when the user inputs the game number.
# For example - if the user says that he wants to see how Game 3 was played, you should print out all the moves on the board and print out the winner at the end of the game.

##################################################################################################################################################################################################################


print("Welcome To Game of TIC TAC TOE\n")
n = int(input("please enter number of Game rounds: "))


def display_board():
    print('\t' + board[1] + '\t|\t' + board[2] + '\t|\t' + board[3])
    print('\t----+-------+----')
    print('\t' + board[4] + '\t|\t' + board[5] + '\t|\t' + board[6])
    print('\t----+-------+----')
    print('\t' + board[7] + '\t|\t' + board[8] + '\t|\t' + board[9])


def user_choice():
    while True:
        ip = input('HUMAN Choose your mark[x/X/o/O]: ')
        if ip in ['x', 'X']:
            print('HUMAN You choose "X".\nHUMAN You play first.')
            return 'x', 'o'
        elif ip in ['O', 'o']:
            print('HUMAN You choose "O".\nSo I get to plays first.')
            return 'o', 'x'
        else:
            print('HUMAN Enter correct input!')


def human_input(mark):
    while True:
        ip = input(f"HUMAN enter your choice to mark '{mark}': ")
        if not ip.isdigit() or int(ip) >= 10 or int(ip) <= 0:
            print("HUMAN  Enter valid option (1 - 9).")
        else:
            ip = int(ip)
            if board[ip] != " ":
                print("HUMAN, place already taken.")
            else:
                return ip


def win_check(human, cpu):
    winning_place = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for win_place in winning_place:
        if board[win_place[0]] == board[win_place[1]] == board[win_place[2]] == human:
            print('HUMAN wins the match!')

            return False
        elif board[win_place[0]] == board[win_place[1]] == board[win_place[2]] == cpu:
            print('CPU wins the match!')

            return False
    if ' ' not in board:
        print('MATCH DRAW!!')

        return False
    return True


def winning(mark, board):
    winning_place = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for win_place in winning_place:
        if board[win_place[0]] == board[win_place[1]] == board[win_place[2]] == mark:
            return True


def win_move(i, board, mark):
    temp_board = list(board)
    temp_board[i] = mark
    if winning(mark, temp_board):
        return True
    else:
        return False


def cpu_input(cpu, human, board):
    for i in range(1, 10):
        if board[i] == ' ' and win_move(i, board, cpu):
            return i
    for i in range(1, 10):
        if board[i] == ' ' and win_move(i, board, human):
            return i
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        if board[i] == ' ':
            return i


def main_game():
    global board

    play = True
    board = ['', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    human, cpu = user_choice()
    display_board()
    while play:
        if human == 'x':
            x = human_input(human)
            board[x] = human
            display_board()
            play = win_check(human, cpu)
            if play:
                o = cpu_input(cpu, human, board)
                print(f'[CPU] Entered:{o}')
                board[o] = cpu
                display_board()
                play = win_check(human, cpu)
        else:
            x = cpu_input(cpu, human, board)
            print(f'[CPU] Entered:{x}')
            board[x] = cpu
            display_board()
            play = win_check(human, cpu)
            if play:
                o = human_input(human)
                board[o] = human
                display_board()
                play = win_check(human, cpu)

    return board
################################################################################################################################################################################################################

game_dict = {}
for i in range(1, n + 1):
    key = i
    a = main_game()
    value = a
    game_dict[key] = value

# print(game_dict)
################################################################################################################################################################################################################

def info():
    r = int(input("Enter the round whose information is required: "))
    print('\t' + game_dict[r][1] + '\t|\t' + game_dict[r][2] + '\t|\t' + game_dict[r][3])
    print('\t----+-------+----')
    print('\t' + game_dict[r][4] + '\t|\t' + game_dict[r][5] + '\t|\t' + game_dict[r][6])
    print('\t----+-------+----')
    print('\t' + game_dict[r][7] + '\t|\t' + game_dict[r][8] + '\t|\t' + game_dict[r][9])




yes = input("Require information about other rounds(y/n): ")
a = True
while a:
    if yes in ['y', 'Y']:
        info()
    elif yes in ['n','N']:
        a = False
        exit()

