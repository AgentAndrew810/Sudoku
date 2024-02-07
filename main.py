import pygame
from menu import Menu
from game import Game
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, BOARD_SIZE, PANEL_SIZE, PADDING

# pygame setup
pygame.init()
clock = pygame.time.Clock()

# change title and icon of window
pygame.display.set_caption("Sudoku")


def main() -> None:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

    # setup objects
    menu = Menu()
    game = Game(screen)

    while game.active:
        for event in pygame.event.get():
            # if the user hits the x button quit the application
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            elif event.type == pygame.VIDEORESIZE:
                width, height = event.size
                
                # get the minimum dimensions
                min_width = BOARD_SIZE + PADDING * 3 + PANEL_SIZE
                min_height = BOARD_SIZE + PADDING * 2
                
                # adjust the screen and reset the sizes of items in the game class
                screen = pygame.display.set_mode((max(min_width, width), max(min_height, height)), pygame.RESIZABLE)
                game.set_sizes((max(min_width, width), max(min_height, height)))

        game.draw(screen)
        pygame.display.flip()


# run the program
if __name__ == "__main__":
    main()
