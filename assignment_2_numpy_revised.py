'''
 A Tic Tac Toe Game - revised with numpy

Problem Statement
#################
Create a Tic Tac Toe game.
Here are the requirements:
Two players should be able to play the game (user, computer)
The board should be printed out every time a player makes a move
You should be able to accept input of the player position and then place a symbol on the board
- Store the Game logs (info about the moves, result) for 10 games into a data structure.
- You should be able to recreate the moves and print out the board for each of the moves for any of the 10 games when the user inputs the game number.
For example - if the user says that he wants to see how Game 3 was played, you should print out all the moves on the board and print out the winner at the end of the game.

basic requirements
>no of rounds
>game board
>reference board
>player symbol choice
>players turn choice
>position marking
>checking position availability
>winning condition[win,lose,draw]
'''
########################################################################################################################

import random
import numpy as np


def no_of_rounds():
    n = ' '
    while n.isdigit() is False:
        n = input("Enter the no of rounds you want to play!: ")
        if n.isdigit() != False:
            return int(n)
            break
        else:
            print('Enter a valid integer')


def reference_board():
    ref = np.array(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
    for i in range(0, len(ref), 3):
        print('\t' + ref[i] + '\t|\t' + ref[i + 1] + '\t|\t' + ref[i + 2])
        if i != 6:
            print('\t----+-------+----')


def display_board(board):
    for i in range(1, len(board), 3):
        print('\t' + board[i] + '\t|\t' + board[i + 1] + '\t|\t' + board[i + 2])
        if i != 7:
            print('\t----+-------+----')


def player_input():
    h_ = ' '
    while h_ not in np.array(['X', 'O', 'x', 'o']):
        h_ = input('Human, Do you want your mark to be X or O? ')
        if h_ not in np.array(['X', 'O', 'x', 'o']):
            print("Invalid Marker!!")
    h_ = h_.upper()
    if h_ == 'X':
        c_ = 'O'
    elif h_ == 'O':
        c_ = 'X'
    return h_,c_


def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal

# def win_check(board, mark):
#     for index in winning_combinations:
#         if board[index][0] == board[index][1] == board[index][2] == mark:
#             return True


def choose_first():
    if random.randint(0, 1) == 0:
        return 'human'
    else:
        return 'cpu '


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))

    return position


def pc_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = random.randint(1, 9)

    return position


########################################################################################################################
def ttt():

    winning_combinations = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]])
    r = no_of_rounds()
    a = 0
    w = 0
    while a != r:

        x = 0
        j = 0
        round_history = np.array([[0] * 9] * 10)
        user_input = np.array([''] * 10)
        history_board = np.array([' '] * 10)
        winner_stat = [' ']*10
        print('\tWelcome to Tic Tac Toe!\n')
        print('\tReference Board\n')
        reference_board()

        # Reset the board
        board = np.array(['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])

        position_history = np.array([0] * 9)
        i = 0


        human, cpu = player_input()
        # user_input[j] = human
        turn = choose_first()
        if turn == 'human':
            user_input[j] = human
        else:
            user_input[j] = cpu

        play_game = input('Are you ready to play? Enter Y or N.')

        if play_game == 'y' or 'Y':
            game_on = True
        else:
            game_on = False

        while game_on:
            if turn == 'human':
                position = player_choice(board)
                place_marker(board, human, position)
                print("\tHuman's Move\n")
                display_board(board)
                position_history[i] = position
                i=i+1

                if win_check(board, human):
                    print("\tHumans's Winnnig Move\n")
                    display_board(board)
                    print('Congratulations! You have won the game!')
                    winner_stat[w] = 'human'
                    game_on = False
                else:
                    if full_board_check(board):
                        print("\tTie Board\n")
                        display_board(board)
                        print('The game is a draw!')
                        winner_stat[w] = 'draw'

                        break
                    else:
                        turn = 'cpu'

            else:
                # Player2's turn.

                position = pc_choice(board)
                place_marker(board, cpu, position)
                print("\tCPU's Move\n")
                display_board(board)
                position_history[i] = position
                i=i+1

                if win_check(board, cpu):
                    print("\tCPU's Winnnig Move\n")
                    display_board(board)
                    print('CPU has won!')
                    winner_stat[w] = 'cpu'

                    game_on = False
                else:
                    if full_board_check(board):
                        print("\tTie Board\n")
                        display_board(board)
                        print('The game is a draw!')
                        winner_stat[w] = 'draw'

                        break
                    else:
                        turn = 'human'
        a += 1
        round_history[j] = position_history
        j = j + 1
        w=w+1


    # print(winner_stat)
    round_no = int(input("enter round for which you need information: "))
    print(f'winner of the round is {winner_stat[round_no-1]}')

    if user_input[round_no - 1] == '':
        print("no round")
    if user_input[round_no - 1] == 'X':
        for item in range(0, len(round_history[round_no - 1])):
            if round_history[round_no - 1][item] == 0:
                break
            else:
                if x == 0:
                    history_board[round_history[round_no - 1][item]] = 'X'
                    display_board(history_board)
                    x = 1

                elif x == 1:
                    history_board[round_history[round_no - 1][item]] = 'O'
                    display_board(history_board)
                    x = 0
    elif user_input[round_no - 1] == 'O':
        # print(round_history[round_no - 1])
        for item in range(0, len(round_history[round_no - 1])):
            if round_history[round_no - 1][item] == 0:
                break
            else:
                if x == 0:
                    history_board[round_history[round_no - 1][item]] = 'O'
                    display_board(history_board)
                    x = 1

                elif x == 1:
                    history_board[round_history[round_no - 1][item]] = 'X'
                    display_board(history_board)
                    x = 0

########################################################################################################################

ttt()
