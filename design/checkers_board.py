"""
This is a problem I found in one of the video interviews for system design in interviewing.io

"""
from enum import Enum
from typing import List


class Color(Enum):
    UNKNOWN = 'U',
    RED = 'R',
    WHITE = 'W'

class Piece:
    def __init__(self, x, y, color: Color):
        self.x = 0
        self.y = 0
        self.color = color

    @property
    def __repr__(self):
        return "{}{}{}".format(self.x, self.y, self.color.name)


class Board:
    def __init__(self, size: int):
        self.size = size
        self.grid = []
        for _ in range(size):
            self.grid.append([None] * size)

    def __validate_list_of_pieces(self, list_of_pieces: List[Piece]) -> bool:
        check = [[False] * self.size for _ in range(self.size)]
        for piece in list_of_pieces:
            # validate coordinates
            if piece.x > self.size or piece.y > self.size:
                return False
            if not check[piece.x][piece.y] and self.grid[piece.x][piece.y] == None:
                check[piece.x][piece.y] = True
                return True
            else:
                return False


    def place_pieces(self, list_of_pieces) -> None:
        # validate pieces
        if self.__validate_list_of_pieces(list_of_pieces) == False:
            raise ValueError("Invalid input list of pieces")
        # place the pieces
        for piece in list_of_pieces:
            print(piece)
            self.grid[piece.x][piece.y] = piece

    def print_board(self) -> None:
        for row in range(self.size):
            for col in range(self.size):
                if self.grid[row][col]:
                    print(self.grid[row][col], end="")
                else:
                    print (" ", end="")
            print("\n")


if __name__ == '__main__':
    checkers = Board(8)
    p1 = Piece(0, 4, Color.RED)
    print(p1)
    p2 = Piece(1, 4, Color.RED)
    p3 = Piece(2, 5, Color.RED)
    p4 = Piece(3, 7, Color.RED)
    checkers.place_pieces([p1,p2,p3,p4])
    checkers.print_board()
