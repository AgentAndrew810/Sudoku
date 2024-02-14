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

    def darken(self) -> tuple[int, int, int]:
        r = self.colour[0]
        g = self.colour[1]
        b = self.colour[2]

        return (r * 0.8, g * 0.8, b * 0.8)

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
        x, y = pygame.mouse.get_pos()
        if self.is_over(x, y):
            colour = self.darken()
        else:
            colour = self.colour
        
        pygame.draw.rect(screen, colour, (self.x, self.y, self.width, self.height))
