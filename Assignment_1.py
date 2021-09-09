# Assignment Question

# Make a two-player Rock-Paper-Scissors game. One of the players is the computer.
#
# 10 rounds. Print out the winner and points earned by both players at the end of the game.
#
# Remember the rules:
#
# Rock beats Scissors
# Scissors beats Paper
# Paper beats Rock
#
#
# Use a dictionary to store the history of choices made by the Player and the Computer.
#
#
# You should be able to print the choices made by the Player and the Computer in each round once the game is completed.
#
#
# Example -
#
#
#
# Enter the round for which you need the information >> 3
#
#
# Output
#
#
# Player choice = Rock
#
# Computer choice = Paper
#
# Player won Round 3
#
#
# * Please make sure that you use the appropriate control, data structures to ensure that the space, time complexity and number of lines of code are kept to a minimum.

import random

p1 = 0
p2 = 0
for i in range(1,11):
    Human = input("Enter your choice Human (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    Computer = random.choice(possible_actions)
    game_dict = {"round": [], "choices": {'Human': [], 'Computer': []}}

    if Human == Computer:
        print("it's a tie!")

    elif Human == "rock" and Computer == "paper":
        p2 = p2 + 1

    elif Human == "rock" and Computer == "scissors":
        p1 = p1 + 1

    elif Human == "paper" and Computer == "rock":
        p1 = p1 + 1

    elif Human == "paper" and Computer == "scissors":
        p2 = p2 + 1

    elif Human == "scissors" and Computer == "paper":
        p1 = p1 + 1

    elif Human == "scissors" and Computer == " rock":
        p2 = p2 + 1

    game_dict["round"].append(i)
    game_dict["choices"]["Human"].append(Human)
    game_dict["choices"]["Computer"].append(Computer)
    print(game_dict)


print("\n")
if p1 == p2:
    print("It's a Tie!\n")
elif p1>p2:
    print('Human is the WINNER!!\n')
else:
    print('Computer is the WINNER!!\n')

print('\tPOINT TABLE\n')
print('{0:8} | {1:9}'.format('Players', 'Points'))
print('{0:8} | {1:5}'.format('Human', p1))
print('{0:8} | {1:5}'.format('Computer', p2))

