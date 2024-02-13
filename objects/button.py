import pygame


class Button:
    def __init__(
        self, x: int, y: int, width: int, height: int, colour: tuple[int, int, int]
    ) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour

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
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.width, self.height))
