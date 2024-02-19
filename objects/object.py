import pygame


class Object:
    instances = []

    def __init__(self) -> None:
        self.instances.append(self)

    @classmethod
    def set_sizes(cls, sizes: dict[str:int]) -> None:
        cls.cell_size = sizes["cell_size"]
        cls.board_size = sizes["board_size"]
        cls.x_padd = sizes["x_padd"]
        cls.y_padd = sizes["y_padd"]
        cls.padd = sizes["padd"]
        cls.line_size = sizes["line_size"]
        cls.big_line_size = sizes["big_line_size"]

        cls.font = pygame.font.SysFont(None, sizes["font_size"])

        for instance in cls.instances:
            if hasattr(instance, "update"):
                instance.update()
