import pygame
from utils.get_sizes import get_sizes
from sudoku import Sudoku
from constants import WHITE, YELLOW, BLUE, BLACK


class Board:
    def __init__(self, screen: pygame.surface.Surface, difficulty=0.5) -> None:
        self.original = Sudoku(3).difficulty(difficulty).board
        self.nums = [row.copy() for row in self.original]
        self.status = [[None for _ in range(9)] for _ in range(9)]
        self.selected = (None, None)
        
        sizes = get_sizes(*screen.get_size())
        self.set_sizes(sizes)

    def set_sizes(self, sizes: dict[str, int]) -> None:
        self.__dict__.update(sizes)

        self.font = pygame.font.SysFont(None, self.font_size)

    def get_x(self, col: int) -> None:
        return self.x_padd + col * self.cell_size

    def get_y(self, row: int) -> None:
        return self.y_padd + row * self.cell_size

    def is_over(self, x: int, y: int) -> bool:
        if (
            x >= self.x_padd
            and y >= self.y_padd
            and x <= self.x_padd + self.board_size
            and y <= self.y_padd + self.board_size
        ):
            return True
        else:
            return False

    def select(self, x: int, y: int) -> None:
        # find the row and col
        row = (y - self.y_padd) // self.cell_size
        col = (x - self.x_padd) // self.cell_size

        # select that square
        self.selected = (row, col)

    def move(self, direction: str) -> None:
        if self.selected:
            row, col = self.selected

            # move the selected square based on the direction
            if direction == "left":
                col = max(0, col - 1)
            elif direction == "right":
                col = min(8, col + 1)
            elif direction == "up":
                row = max(0, row - 1)
            elif direction == "down":
                row = min(8, row + 1)

        self.selected = (row, col)

    def edit(self, number: int) -> None:
        if self.selected:
            row, col = self.selected

            # if that number isn't on the original board
            if self.original[row][col] is None:
                self.nums[row][col] = number

    def draw(self, screen: pygame.surface.Surface) -> None:
        # draw squares and numbers
        for row in range(9):
            for col in range(9):
                # get the colour of the square based on the status
                if (row, col) == self.selected:
                    colour = YELLOW
                elif self.original[row][col]:
                    colour = BLUE
                else:
                    colour = WHITE

                pygame.draw.rect(
                    screen,
                    colour,
                    (
                        self.get_x(col),
                        self.get_y(row),
                        self.cell_size,
                        self.cell_size,
                    ),
                )

                # get the number on that square
                number = self.nums[row][col]

                # if there is a number draw it on the square
                if number:
                    width, height = self.font.size(str(number))
                    font_surf = self.font.render(str(number), True, BLACK)
                    screen.blit(
                        font_surf,
                        (
                            self.get_x(col + 0.5) - width // 2,
                            self.get_y(row + 0.5) - height // 2,
                        ),
                    )

        # draw lines
        for i in range(10):
            line_width = self.big_line_size if i % 3 == 0 else self.line_size

            # vertical lines
            pygame.draw.line(
                screen,
                BLACK,
                (self.get_x(i), self.y_padd),
                (self.get_x(i), self.y_padd + self.board_size),
                line_width,
            )
            # horizontal lines
            pygame.draw.line(
                screen,
                BLACK,
                (self.x_padd, self.get_y(i)),
                (self.x_padd + self.board_size, self.get_y(i)),
                line_width,
            )
