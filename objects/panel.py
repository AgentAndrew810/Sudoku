import pygame
from constants import BLACK


class Panel:
    def __init__(self) -> None:
        return

    def set_sizes(self, sizes: dict[str, int]) -> None:
        self.__dict__.update(sizes)
        
        self.x = self.x_padd + self.board_size + self.padd
        self.y = self.y_padd
        self.width = self.cell_size * 2
        self.height = self.board_size

    def draw(self, screen: pygame.surface.Surface) -> None:
        pygame.draw.rect(
            screen,
            BLACK,
            (self.x, self.y, self.width, self.height),
            self.big_line_size,
        )
