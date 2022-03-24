from dataclasses import dataclass
from enum import Enum
from tabulate import tabulate
from aenum import MultiValueEnum
import string

BOARD_RANGE = range(0, 64, 8)

NEW_GAME_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
RANDOM_POS_FEN = "r1b1k1nr/p2p1pNp/n2B4/1p1NP2P/6P1/3P1Q2/P1P1K3/q5b1"


class Type(MultiValueEnum):
    _init_ = "value code"
    EMPTY = 0, "e"
    KING = 1, "k"
    PAWN = 2, "p"
    KNIGHT = 3, "n"
    BISHOP = 4, "b"
    ROOK = 5, "r"
    QUEEN = 6, "q"


class Color(Enum):
    BLACK = 0
    WHITE = 1


unicode_pieces = {
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
        self.board = []
        self.initialize_board()
        self.initialize_unicode_board()

    def initialize_board(self):
        for rank in NEW_GAME_FEN.split("/"):
            for char in rank:
                if char == " ":
                    break
                elif char in "12345678":
                    self.board.extend([None] * int(char))
                else:
                    self.board.append(
                        Piece(
                            type=Type(char.lower()),
                            color=Color.WHITE if char.isupper() else Color.BLACK,
                        )
                    )

    def initialize_unicode_board(self):
        self.unicode_board = []
        for i, rank in enumerate([self.board[x : x + 8] for x in BOARD_RANGE]):
            for j, piece in enumerate(rank):
                unicode = (
                    (piece.color, piece.type)
                    if piece
                    else (Color((i + j) % 2), Type.EMPTY)
                )
                self.unicode_board.append(unicode_pieces[unicode])

    def __repr__(self) -> str:
        return tabulate(
            [self.board[x : x + 8] for x in BOARD_RANGE],
            tablefmt="grid",
            stralign="center",
            headers=string.ascii_lowercase[:8],
            showindex=range(8, 0, -1),
        )


board = Board()
print(board)
