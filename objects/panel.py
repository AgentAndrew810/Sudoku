import pygame
from objects.button import Button
from utils.get_sizes import get_sizes
from constants import BLACK, BLUE


class Panel:
    def __init__(self, screen: pygame.surface.Surface) -> None:
        sizes = get_sizes(*screen.get_size())
        self.set_sizes(sizes)
        
        self.buttons = {
            "solve": Button(self.x, self.y, self.width, self.height // 3, BLUE)
        }
        

    def set_sizes(self, sizes: dict[str, int]) -> None:
        self.__dict__.update(sizes)

        self.x = self.x_padd + self.board_size + self.padd
        self.y = self.y_padd
        self.width = self.cell_size * 2
        self.height = self.board_size
        
    def select(self, x: int, y: int) -> None:
        return

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
            
        pygame.draw.rect(
            screen,
            BLACK,
            (self.x, self.y, self.width, self.height),
            self.big_line_size,
        )
