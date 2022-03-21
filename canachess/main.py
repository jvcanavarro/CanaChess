import pygame

WIDTH = 512
HEIGHT = 512
DISPLAY_SIZE = (WIDTH, HEIGHT)

DIMENSION = 8
SQUARE_SIZE = HEIGHT // DIMENSION

PIECES = ["bB", "bK", "bN", "bp", "bQ", "bR", "wB", "wK", "wN", "wp", "wQ", "wR"]
IMAGES = {}

FPS = 15


class Move:
    rank_to_row = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}
    file_to_col = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}

    row_to_rank = {value: key for key, value in rank_to_row.items()}
    col_to_file = {value: key for key, value in file_to_col.items()}

    def __init__(self, start_pos, end_pos, board) -> None:
        self.start_row, self.start_col = start_pos[0], start_pos[1]
        self.end_row, self.end_col = end_pos[0], end_pos[1]
        self.moved_piece = board[self.start_row][self.start_col]
        self.captured_piece = board[self.end_row][self.end_col]

    def get_chess_notation(self):
        return self.get_rank_file(self.start_row, self.start_col) + self.get_rank_file(
            self.end_row, self.end_col
        )

    def get_rank_file(self, col, row):
        return self.col_to_file[col] + self.row_to_rank[row]


class Match:
    board = [
        ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
        ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
        ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
    ]
    is_white_turn: bool = True
    moves_log: list = []

    def make_move(self, move: Move):
        self.board[move.start_row][move.start_col] = "--"
        self.board[move.end_row][move.end_col] = move.moved_piece
        self.moves_log.append(move)
        self.is_white_turn = not self.is_white_turn


def load_piece_images():
    for piece in PIECES:
        image = pygame.image.load(f"../images/{piece}.png")
        IMAGES[piece] = pygame.transform.scale(image, (SQUARE_SIZE, SQUARE_SIZE))


def draw_squares(screen):
    colors = [pygame.Color("white"), pygame.Color("orange")]
    for i in range(DIMENSION):
        for j in range(DIMENSION):
            pygame.draw.rect(
                screen,
                colors[(i + j) % 2],
                pygame.Rect(j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),
            )


def draw_pieces(screen, board):
    for i in range(DIMENSION):
        for j in range(DIMENSION):
            piece = board[i][j]
            if piece != "--":
                screen.blit(
                    IMAGES[piece],
                    pygame.Rect(
                        j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE
                    ),
                )


def main():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY_SIZE)
    clock = pygame.time.Clock()
    screen.fill(pygame.Color("white"))

    match = Match()

    load_piece_images()

    running = True
    selected_square = ()
    player_clicks = []
    while running:
        for event in pygame.event.get():
            running = event.type != pygame.QUIT
            if event.type == pygame.MOUSEBUTTONDOWN:

                location = pygame.mouse.get_pos()
                col = location[0] // SQUARE_SIZE
                row = location[1] // SQUARE_SIZE

                if selected_square == (row, col):
                    selected_square = ()
                    player_clicks = []
                else:
                    selected_square = (row, col)
                    player_clicks.append(selected_square)

                if len(player_clicks) == 2:
                    move = Move(player_clicks[0], player_clicks[1], match.board)
                    print(move.get_chess_notation())
                    match.make_move(move)
                    selected_square = ()
                    player_clicks = []

        draw_squares(screen)
        draw_pieces(screen, match.board)

        clock.tick(FPS)
        pygame.display.flip()


if __name__ == "__main__":
    main()
