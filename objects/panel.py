import pygame
from objects.button import Button
from objects.clock import Clock
from objects.object import Object
from constants import BLACK, BLUE, YELLOW, RED


class Panel(Object):
    def __init__(self) -> None:
        super().__init__()
        self.update(True)

    def select(self, x: int, y: int) -> str | None:
        for name, button in self.buttons.items():
            if button.is_over(x, y):
                return name

    def update(self, new_clock: bool = False) -> None:
        self.x = self.x_padd + self.board_size + self.padd
        self.y = self.y_padd
        self.width = self.cell_size * 2
        self.height = self.board_size

        # create a new clock or change the position of the clock
        if new_clock:
            self.clock = Clock(self.x, self.y, self.width, self.cell_size * 3)
        else:
            self.clock.change_position(self.x, self.y, self.width, self.cell_size * 3)

        # recreate all the buttons
        self.buttons = {
            "hint": Button(
                self.x,
                self.y + self.cell_size * 3,
                self.width,
                self.cell_size * 2,
                YELLOW,
            ),
            "solve": Button(
                self.x,
                self.y + self.cell_size * 5,
                self.width,
                self.cell_size * 2,
                BLUE,
            ),
            "end": Button(
                self.x, self.y + self.cell_size * 7, self.width, self.cell_size * 2, RED
            ),
        }

    def draw(self, screen: pygame.surface.Surface) -> None:
        # draw all the buttons
        for button in self.buttons.values():
            button.draw(screen)

        # draw clock
        self.clock.draw(screen)

        # draw the panel
        pygame.draw.rect(
            screen,
            BLACK,
            (self.x, self.y, self.width, self.height),
            self.big_line_size,
        )
