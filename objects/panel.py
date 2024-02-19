import pygame
from objects.button import Button
from objects.clock import Clock
from objects.object import Object
from constants import BLACK, BLUE


class Panel(Object):
    def __init__(self) -> None:
        super().__init__()
        self.update(True)

    def select(self, x: int, y: int) -> str | None:
        for name, button in self.buttons.items():
            if button.is_over(x, y):
                return name

    def is_over(self, x: int, y: int) -> bool:
        if (
            x >= self.x
            and y >= self.y
            and x <= self.x + self.width
            and y <= self.y + self.height
        ):
            return True
        else:
            return False

    def update(self, new_clock: bool = False) -> None:
        self.x = self.x_padd + self.board_size + self.padd
        self.y = self.y_padd
        self.width = self.cell_size * 2
        self.height = self.board_size

        # create a new clock or change the position of the clock
        if new_clock:
            self.clock = Clock(self.x, self.y, self.width, self.height // 3)
        else:
            self.clock.change_position(self.x, self.y, self.width, self.height // 3)

        # recreate all the buttons
        self.buttons = {
            "solve": Button(
                self.x,
                self.y + self.height // 3,
                self.width,
                self.height // 3,
                BLUE,
            )
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
