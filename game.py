import pygame
from objects.board import Board
from objects.panel import Panel
from utils.get_sizes import get_sizes
from constants import ARROWS, NUMBERS, WHITE


class Game:
    def __init__(self, screen: pygame.surface.Surface) -> None:
        self.active = True
        self.board = Board()
        self.panel = Panel()

        sizes = get_sizes(*screen.get_size())
        self.set_sizes(sizes)

    def set_sizes(self, sizes: dict[str, int]) -> None:
        self.__dict__.update(sizes)
        
        self.board.set_sizes(sizes)
        self.panel.set_sizes(sizes)

    def click(self, x: int, y: int) -> None:
        if self.board.is_over(x, y):
            self.board.select(x, y)

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
        self.panel.draw(screen)
