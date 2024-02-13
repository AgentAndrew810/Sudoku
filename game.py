import pygame
from board import Board
from utils.get_sizes import get_sizes
from constants import ARROWS, NUMBERS, BLACK, WHITE


class Game:
    def __init__(self, screen: pygame.surface.Surface) -> None:
        self.active = True
        self.board = Board()

        sizes = get_sizes(*screen.get_size())
        self.set_sizes(sizes)

    def set_sizes(self, sizes: dict[str, int]) -> None:
        self.__dict__.update(sizes)
        self.board.set_sizes(sizes)

    def click(self, x: int, y: int) -> None:
        # if the cursor is on the board
        if (
            x >= self.x_padd
            and x <= self.x_padd + self.board_size
            and y >= self.y_padd
            and y <= self.y_padd + self.board_size
        ):
            # find the row and col
            row = (y - self.y_padd) // self.cell_size
            col = (x - self.x_padd) // self.cell_size

            # highlight that square
            self.board.highlighted = [row, col]

    def press_key(self, key: int) -> None:
        for arrow in ARROWS:
            if key == arrow:
                self.board.move(ARROWS[arrow])

        for number in NUMBERS:
            if key == number:
                self.board.edit(NUMBERS[number])

    def draw(self, screen: pygame.surface.Surface) -> None:
        # draw a white background
        screen.fill(WHITE)

        self.board.draw(screen)

        self.panel_start = self.x_padd + self.board_size + self.padd
        self.panel_width = self.cell_size * 2

        # panel border
        pygame.draw.rect(
            screen,
            BLACK,
            (self.panel_start, self.y_padd, self.panel_width, self.board_size),
            self.big_line_size,
        )
