import pygame
from game import Game
from objects.object import Object
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, MIN_WIDTH, MIN_HEIGHT

# pygame setup
pygame.init()

# change title and icon of window
pygame.display.set_caption("Sudoku")
pygame.display.set_icon(pygame.image.load("assets/images/icon.svg"))


def main() -> None:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
    Object.set_sizes(SCREEN_WIDTH, SCREEN_HEIGHT)
    game = Game()

    while game.active:
        for event in pygame.event.get():
            # if the user hits the x button quit the application
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            elif event.type == pygame.VIDEORESIZE:
                width, height = event.size

                # choose the bigger option
                width = max(width, MIN_WIDTH)
                height = max(height, MIN_HEIGHT)

                # adjust the screen and reset the sizes in the objects
                screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
                Object.set_sizes(width, height)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                game.click(*event.pos)

            elif event.type == pygame.KEYDOWN:
                game.press_key(event.key)

        # update the screen
        game.draw(screen)
        pygame.display.flip()


# run the program
if __name__ == "__main__":
    main()
