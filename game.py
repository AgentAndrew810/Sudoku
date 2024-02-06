import pygame
from board import Board
from constants import BLACK, WHITE, BLUE, PANEL_SIZE, PADDING


class Game:
    def __init__(self, screen: pygame.surface.Surface) -> None:
        self.active = True
        self.board = Board()
        self.set_sizes(screen.get_size())

    def set_sizes(self, size: tuple[int, int]) -> None:
        # get the full width and height of the screen
        self.full_width, self.full_height = size

        # calculate the available width and height
        available_width = self.full_width - PADDING * 2 - PANEL_SIZE
        available_height = self.full_height - PADDING * 2

        # set default values of padding
        self.x_padd = PADDING
        self.y_padd = PADDING

        if available_width > available_height:
            # if the available width is greater than the height, calculate cell_size from height, add extra x padding
            self.cell_size = available_height // 9
            self.x_padd += (available_width - available_height) // 2
        else:
            # if the available height is greater than the width, calculate cell_size from width, add extra y padding
            self.cell_size = available_width // 9
            self.y_padd += (available_height - available_width) // 2

        # get the size of the board
        self.board_size = self.cell_size * 9

        # get the size of a big cell
        self.big_cell_size = self.cell_size*3

    def x_coord(self, x):
        return self.x_padd + x * self.cell_size

    def y_coord(self, y):
        return self.y_padd + y * self.cell_size

    def draw(self, screen: pygame.surface.Surface) -> None:
        # draw a white background
        screen.fill(WHITE)

        # draw inside lines
        for i in range(10):
            # vertical lines
            pygame.draw.line(screen, BLACK, (self.x_coord(i), self.y_padd), (self.x_coord(i), self.y_padd + self.board_size))
            # horizontal lines
            pygame.draw.line(screen, BLACK, (self.x_padd, self.y_coord(i)), (self.x_padd + self.board_size, self.y_coord(i)))
            
        # draw outside lines
        for i in range(4):
            # vertical lines
            pygame.draw.line(screen, BLACK, (self.big_cell_size*i+self.x_padd, self.y_padd), (self.big_cell_size*i+self.x_padd, self.y_padd+self.board_size), 5)
            # horizontal lines
            pygame.draw.line(screen, BLACK, (self.x_padd, self.big_cell_size*i+self.x_padd), (self.x_padd + self.board_size, self.big_cell_size*i+self.x_padd), 5)
