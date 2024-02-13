import pygame
from sudoku import Sudoku
from constants import WHITE, YELLOW, BLUE, BLACK


class Board:
    def __init__(self, difficulty=0.5) -> None:
        self.original = Sudoku(3).difficulty(difficulty).board
        self.nums = [row.copy() for row in self.original]
        self.status = [[None for _ in range(9)] for _ in range(9)]
        self.highlighted = None

    def set_sizes(self, sizes: dict[str, int]) -> None:
        self.__dict__.update(sizes)
        self.font = pygame.font.SysFont(None, self.font_size)

    def get_x(self, col: int) -> None:
        return self.x_padd + col * self.cell_size

    def get_y(self, row: int) -> None:
        return self.y_padd + row * self.cell_size

    def move(self, direction: str) -> None:
        # move the highlighted square based on the direction
        if self.highlighted:
            if direction == "left":
                if not self.highlighted[1] == 0:
                    self.highlighted[1] -= 1
            elif direction == "right":
                if not self.highlighted[1] == 8:
                    self.highlighted[1] += 1
            elif direction == "up":
                if not self.highlighted[0] == 0:
                    self.highlighted[0] -= 1
            elif direction == "down":
                if not self.highlighted[0] == 8:
                    self.highlighted[0] += 1

    def edit(self, number: int) -> None:
        if self.highlighted:
            row, col = self.highlighted

            # if that number isn't on the original board
            if self.original[row][col] is None:
                self.nums[row][col] = number

    def draw(self, screen: pygame.surface.Surface) -> None:
        # draw squares and numbers
        for row in range(9):
            for col in range(9):
                # get the colour of the square based on the status
                if [row, col] == self.highlighted:
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
