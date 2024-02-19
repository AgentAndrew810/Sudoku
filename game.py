import pygame
from objects.board import Board
from objects.panel import Panel
from constants import ARROWS, NUMBERS, WHITE


class Game:
    def __init__(self) -> None:
        self.active = True

        self.board = Board()
        self.panel = Panel()

    def click(self, x: int, y: int) -> None:
        if self.board.is_over(x, y):
            self.board.select(x, y)

        if self.panel.is_over(x, y):
            button_pressed = self.panel.select(x, y)

            if button_pressed == "solve":
                pass

    def press_key(self, key: int) -> None:
        if key in ARROWS:
            self.board.move(ARROWS[key])

        if key in NUMBERS:
            self.board.edit(NUMBERS[key])

    def draw(self, screen: pygame.surface.Surface) -> None:
        # draw a white background
        screen.fill(WHITE)

        self.board.draw(screen)
        self.panel.draw(screen)
