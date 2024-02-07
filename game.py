import pygame
from board import Board
from constants import BLACK, WHITE, BLUE, PADDING


class Game:
    def __init__(self, screen: pygame.surface.Surface) -> None:
        self.active = True
        self.board = Board()
        self.set_sizes(screen.get_size())

    def set_sizes(self, size: tuple[int, int]) -> None:
        # get the full width and height of the screen
        self.full_width, self.full_height = size
        
        # set the panel width to 1/4 of the width
        self.panel_width = 1/4 * self.full_width

        # calculate the available width and height, by removing padding and panel width
        available_width = self.full_width - PADDING * 3 - self.panel_width
        available_height = self.full_height - PADDING * 2

        # set default values of padding
        self.x_padd = PADDING
        self.y_padd = PADDING

        if available_width > available_height:
            # if the available width is greater than the height, calculate cell_size from height, add more x padd
            self.cell_size = available_height // 9
            self.x_padd += (available_width - available_height) // 3
        else:
            # if the available height is greater than the width, calculate cell_size from width, add more y padd
            self.cell_size = available_width // 9
            self.y_padd += (available_height - available_width) // 2
            
        # calculate helper values (not required by simplify code)
        self.big_cell_size = self.cell_size*3
        self.board_size = self.cell_size*9
        self.panel_start = self.x_padd+self.board_size+self.x_padd


    def x_coord(self, x):
        return self.x_padd + x * self.cell_size

    def y_coord(self, y):
        return self.y_padd + y * self.cell_size

    def draw(self, screen: pygame.surface.Surface) -> None:
        # draw a white background
        screen.fill(WHITE)
        
        # panel border      
        pygame.draw.rect(screen, BLACK, (self.panel_start, self.y_padd, self.panel_width, self.board_size), 5)

        # draw inside lines
        for i in range(10):
            # vertical lines
            pygame.draw.line(screen, BLACK, (self.x_coord(i), self.y_padd), (self.x_coord(i), self.y_padd + self.board_size))
            # horizontal lines
            pygame.draw.line(screen, BLACK, (self.x_padd, self.y_coord(i)), (self.x_padd + self.board_size, self.y_coord(i)))

        # draw outside lines
        for i in range(4):
            # vertical lines
            pygame.draw.line(
                screen,
                BLACK,
                (self.x_padd + self.big_cell_size * i, self.y_padd),
                (self.x_padd + self.big_cell_size * i, self.y_padd + self.board_size),
                5
            )
            # horizontal lines
            pygame.draw.line(
                screen,
                BLACK,
                (self.x_padd, self.y_padd + self.big_cell_size * i),
                (self.x_padd + self.board_size, self.y_padd + self.big_cell_size * i),
                5
            )
