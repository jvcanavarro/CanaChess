import pygame

WIDTH = 512
HEIGHT = 512
DISPLAY_SIZE = (WIDTH, HEIGHT)

DIMENSION = 8
SQUARE_SIZE = HEIGHT // DIMENSION

PIECES = ["bB", "bK", "bN", "bp", "bQ", "bR", "wB", "wK", "wN", "wp", "wQ", "wR"]
IMAGES = {}

FPS = 15


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
    isWhiteTurn: bool = True


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
                    pygame.Rect(j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),
                )


def main():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY_SIZE)
    clock = pygame.time.Clock()
    screen.fill(pygame.Color("white"))

    match = Match()

    load_piece_images()

    running = True
    while running:
        for event in pygame.event.get():
            running = event.type != pygame.QUIT

        draw_squares(screen)
        draw_pieces(screen, match.board)

        clock.tick(FPS)
        pygame.display.flip()


if __name__ == "__main__":
    main()
