import pygame
import time
from constants import BLACK


class Clock:
    def __init__(
        self, x: int, y: int, width: int, height: int, sizes: dict[str, int]
    ) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.initial_time = time.time()
        self.set_sizes(sizes)

    def set_sizes(self, sizes: dict[str, int]) -> None:
        self.__dict__.update(sizes)

        self.font = pygame.font.SysFont(None, self.font_size)

    def draw(self, screen: pygame.surface.Surface) -> None:
        seconds = round(time.time()-self.initial_time)
        minutes, seconds = divmod(seconds, 60)

        displayed_time = f"{minutes:02d}:{seconds:02d}"

        width, height = self.font.size(displayed_time)
        font_surf = self.font.render(displayed_time, True, BLACK)
        screen.blit(
            font_surf,
            (
                self.x + self.width // 2 - width // 2,
                self.y + self.height // 2 - height // 2,
            ),
        )
