import pygame
from game import Game
from utils.get_sizes import get_sizes
from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    MIN_WIDTH,
    MIN_HEIGHT,
    ARROWS,
    NUMBERS,
)

# pygame setup
pygame.init()
clock = pygame.time.Clock()

# change title and icon of window
pygame.display.set_caption("Sudoku")


def main() -> None:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

    # setup objects
    game = Game(screen)

    while game.active:
        for event in pygame.event.get():
            # if the user hits the x button quit the application
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            elif event.type == pygame.VIDEORESIZE:
                width, height = event.size

                width = max(width, MIN_WIDTH)
                height = max(height, MIN_HEIGHT)

                # adjust the screen and reset the sizes of items in the game class
                screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
                game.set_sizes(get_sizes(width, height))

            elif event.type == pygame.MOUSEBUTTONDOWN:
                game.select(*event.pos)

            elif event.type == pygame.KEYDOWN:
                for arrow in ARROWS:
                    if event.key == arrow:
                        game.board.move_highlight(ARROWS[arrow])

                for num in NUMBERS:
                    if event.key == num:
                        game.switch(NUMBERS[num])

        game.draw(screen)
        pygame.display.flip()


# run the program
if __name__ == "__main__":
    main()
