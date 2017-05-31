"""
This is a simple tic-tac-toe terminal game with 2 players.
"""
from __future__ import print_function

from tabulate import tabulate

EMPTY_CELL = ''

class Players(object):
    """ This class stores player specific information"""
    def __init__(self, name, icon):
        self.name = name
        self.icon = icon

    def get_name(self):
        return self.name

    def get_icon(self):
        return self.icon

class TicTacToe(object):
    """
    Board Game class
    """
    def __init__(self):
        self.players = 2
        self.players_dict = dict()
        self.board = [[''] * 3 for _ in range(3)]

    def display_board(self):
        print(tabulate(self.board, tablefmt="grid"))

    def player_swap(self, player_num):
        if player_num == 1:
            return 2
        else:
            return 1

    def is_board_full(self):
        # check if the board is full.
        # If not, the game is still ON.
        for row in self.board:
            if EMPTY_CELL in row:
                return False
        return True

    @property
    def game_over(self):
        over = False
        winner_icon = None

        # check if row has all identical icons
        for row in self.board:
            # convert to set to check if all
            # elements in the row are identical
            over = len(set(row)) == 1
            if over:
                if row[0] != EMPTY_CELL:
                    winner_icon = row[0]
                    break
                else:
                    over = False

        if not over:
            # check if any column has all identical icons
            tmp = []
            for col in range(3):
                tmp = [row[col] for row in self.board]
                over = len(set(tmp)) == 1
                if over:
                    # column identical. Winner is column icon
                    if tmp[0] != EMPTY_CELL:
                        winner_icon = tmp[0]
                        break
                    else:
                        over = False

        if over:
            for key, player in self.players_dict.items():
                if player.icon == winner_icon:
                    print("Aaaaaand the WINNER is......, {}".format(player.name))
        else:
            if self.is_board_full():
                print("OhOh! Not again. Its a draw!")
                over = True

        return over

    def game_loop(self):
        player_num = 1

        # outer game loop
        while True:
            while True:
                # retry exception while loop
                try:
                    print ("{}'s move. Enter position: ".format(self.players_dict[player_num].name))
                    r, c = map(int, input().strip().split())
                    if r < 0 or r > 2: raise Exception
                    if c < 0 or c > 2: raise Exception
                except:
                    print ("Invalid position. Try again!")
                    continue
                break

            if self.board[r][c]:
                print ("Position already occupied.")
            else:
                self.board[r][c] = self.players_dict[player_num].icon
                self.display_board()
                if self.game_over:
                    break
                player_num = self.player_swap(player_num)


    def start(self):
        " Player initialization and begin of game loop"
        print ("Welcome to TIC TAC TOE")
        player_num = 1
        icon = None

        while player_num <= 2:
            name = input('Enter player{} name: '.format(player_num))
            if player_num == 1:
                while icon != 'X' and icon != 'O':
                    icon = input("Please choose your icon: X or O: ")
            else:
                icon = 'X' if self.players_dict[1].icon == 'O' else 'O'

            self.players_dict[player_num] = Players(name, icon)
            player_num += 1

        print ("Let the Games begin")
        self.game_loop()


if __name__ == '__main__':
    TicTacToe().start()


