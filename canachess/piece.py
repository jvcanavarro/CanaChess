from dataclasses import dataclass
from enum import Enum
from hashlib import new
from pprint import pprint
from tabulate import tabulate
from aenum import MultiValueEnum
import string


class Type(MultiValueEnum):
    # NONE = 0
    _init_ = "value code"
    EMPTY = 0, "e"
    KING = 1, "k"
    PAWN = 2, "p"
    KNIGHT = 3, "n"
    BISHOP = 4, "b"
    ROOK = 5, "r"
    QUEEN = 6, "q"


class Color(Enum):
    WHITE = 0
    BLACK = 1


chrs = {
    (Color.WHITE, Type.EMPTY): "\u25FB",
    (Color.WHITE, Type.PAWN): "\u265F",
    (Color.WHITE, Type.ROOK): "\u265C",
    (Color.WHITE, Type.KNIGHT): "\u265E",
    (Color.WHITE, Type.BISHOP): "\u265D",
    (Color.WHITE, Type.KING): "\u265A",
    (Color.WHITE, Type.QUEEN): "\u265B",
    (Color.BLACK, Type.EMPTY): "\u25FC",
    (Color.BLACK, Type.PAWN): "\u2659",
    (Color.BLACK, Type.ROOK): "\u2656",
    (Color.BLACK, Type.KNIGHT): "\u2658",
    (Color.BLACK, Type.BISHOP): "\u2657",
    (Color.BLACK, Type.KING): "\u2654",
    (Color.BLACK, Type.QUEEN): "\u2655",
}


@dataclass
class Piece:
    type: Type
    color: Color = None

    def __repr__(self) -> str:
        # return f"{str(self.color.value).zfill(2)}{str(self.type.value).zfill(2)}"
        # return f"{self.type.name}"
        return f"{self.color.name[0]}_{self.type.name}"


class Board:
    def __init__(self):
        self.square = []
        self.initialize_board()
        self.display_board()

    def initialize_board(self):
        new_game_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
        random_pos = "r1b1k1nr/p2p1pNp/n2B4/1p1NP2P/6P1/3P1Q2/P1P1K3/q5b1"
        for rank in new_game_fen.split("/"):
            for char in rank:
                if char == " ":
                    break
                elif char in "12345678":
                    self.square.extend([None] * int(char))
                else:
                    self.square.append(
                        Piece(
                            type=Type(char.lower()),
                            color=Color.WHITE if char.isupper() else Color.BLACK,
                        )
                    )

    def display_board(self):
        for i, pieces in enumerate([self.square[x : x + 8] for x in range(0, 64, 8)]):
            print(i, pieces)

            for piece in pieces:
                print(chrs.get())
            row_strings = [
                chrs.get(tile, chrs[(Color((i + j) % 2), Type.EMPTY)])
                for j, tile in enumerate(piece)
            ]
            print("".join(row_strings))

    def __repr__(self) -> str:
        return tabulate(
            [self.square[x : x + 8] for x in range(0, 64, 8)],
            tablefmt="grid",
            stralign="center",
            headers=string.ascii_lowercase[:8],
            showindex=range(8, 0, -1),
        )


board = Board()
print(board)
