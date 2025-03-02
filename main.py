import random
import numpy as np

game_on = True
starting_game = input("enter any key to start the game:")

first_player = input("enter the names of the first players:")

second_player = input("enter the names of the second players:")

enter_game = int(input(f"1){first_player} or 2){second_player} \n who is choosing the toss just enter the number :"))

winner = None

choice = int(input(f"Player {enter_game}, select 1 for heads or 2 for tails:"))

random_toss = random.randint(2, 2)

x_gamer = ""
o_gamer = ""

for n in range(1, 3):
    if enter_game == n:
        if choice == random_toss:
            winner = enter_game
            print(f"You won the toss Player{winner} can start the game")
        else:
            winner = 3 - enter_game
            print(f"You lost the toss Player{winner} can start the game")

if winner == 1 and enter_game == 1:
    x_gamer = first_player
    o_gamer = second_player
    print(f"{first_player} is assigned to X")
    print(f"{second_player} is assigned with the O")
else:
    x_gamer = second_player
    o_gamer = first_player
    print(f"{first_player} is assigned to O")
    print(f"{second_player} is assigned with the X")

game_display = np.array([["   __|__|__    "],
                         ["   __|__|__   "],
                         ["     |  |     "]
                         ])
print(game_display)
print("Game markings for the tic tac toe")
display_position = np.array([["(0,0),(0,1),(0,2)"],
                             ["(1,0),(1,1),(1,2)"],
                             ["(2,0),(2,1),(2,2)"]])
print(f"Displaying the 'Game Positions' for the markings {display_position}")
game_play = np.array([["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]])


def x_play():
    x_row, x_col = map(int, input(
        f"enter the X position,{x_gamer} according to the game, Just add the number for example 0,0 :").split(
        ","))
    if x_row > 2 and 2 < x_col:
        x_play()
    return x_row, x_col


def o_play():
    o_row, o_col = map(int, input(
        f"enter the o position,{o_gamer} according to the game Just add the number for example 0,0 :").split(","))
    if o_row > 2 and 2 < o_col:
        o_play()
    return o_row, o_col


class TicTacToe:
    def __init__(self, ttt):
        self.game = ttt

    def add_x(self, xp_row, xp_col):
        if self.game[xp_row, xp_col] == "-":
            self.game[xp_row, xp_col] = "X"
        else:
            print("The position is already been taken by the other player")
            x_play()
            self.add_x(xp_row, xp_col)

    def add_o(self, op_row, op_col):
        if self.game[op_row, op_col] == "-":
            self.game[op_row, op_col] = "O"
        else:
            print("The position already been taken by the other player try another position")
            o_play()
            self.add_o(op_row, op_col)

    def display(self):
        print(self.game)

    def check_rows_and_columns(self, xp, op):
        for number in range(3):
            # Check rows
            if np.all(self.game[number, :] == "X"):
                print(f"...................{xp} won the game..................")
                return False
            elif np.all(self.game[number, :] == "O"):
                print(f"...................{op} won the game..................")
                return False

            # Check columns
            if np.all(self.game[:, number] == "X"):
                print(f"...................{xp} won the game..................")
                return False
            elif np.all(self.game[:, number] == "O"):
                print(f"...................{op} won the game..................")
                return False

        return self.diagonal(xp, op)

    def diagonal(self, xp, op):
        if np.all(np.diag(self.game) == "X") or np.all(np.diag(np.fliplr(self.game)) == "X"):
            print(f"...................{xp} won the game..................")
            return False
        elif np.all(np.diag(self.game) == "O") or np.all(np.diag(np.fliplr(self.game)) == "O"):
            print(f"...................{op} won the game..................")
            return False
        return True

game = TicTacToe(game_play)
while game:
    row, col = x_play()
    game.add_x(row, col)
    game.display()
    if game_on:
        game_on = game.check_rows_and_columns(x_gamer, o_gamer)
    rows, cols = o_play()
    game.add_o(rows, cols)
    game.display()
    game_on = game.check_rows_and_columns(x_gamer, o_gamer)
