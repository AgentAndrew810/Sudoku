import pygame
from objects.button import Button
from objects.clock import Clock
from constants import BLACK, BLUE


class Panel:
    def __init__(self, sizes: dict[str:int]) -> None:
        self.set_sizes(sizes)

    def set_sizes(self, sizes: dict[str, int]) -> None:
        self.__dict__.update(sizes)
        
        self.x = self.x_padd + self.board_size + self.padd
        self.y = self.y_padd
        self.width = self.cell_size * 2
        self.height = self.board_size

        self.clock = Clock(self.x, self.y, self.width, self.height // 3, sizes)

        self.buttons = {
            "solve": Button(
                self.x, self.y + self.height // 3, self.width, self.height // 3, BLUE
            )
        }

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

    def draw(self, screen: pygame.surface.Surface) -> None:
        for button in self.buttons.values():
            button.draw(screen)
            
        self.clock.draw(screen)

        pygame.draw.rect(
            screen,
            BLACK,
            (self.x, self.y, self.width, self.height),
            self.big_line_size,
        )
