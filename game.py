import pygame
from board import Board
from utils.get_sizes import get_sizes
from constants import BLACK, WHITE, BLUE, YELLOW


class Game:
    def __init__(self, screen: pygame.surface.Surface) -> None:
        self.active = True
        self.board = Board()

        sizes = get_sizes(*screen.get_size())
        self.set_sizes(sizes)

    def set_sizes(self, sizes: dict[str, int]) -> None:
        self.__dict__.update(sizes)
        self.font = pygame.font.SysFont(None, self.font_size)

    def get_x(self, col: int) -> None:
        return self.x_padd + col * self.cell_size

    def get_y(self, row: int) -> None:
        return self.y_padd + row * self.cell_size

    def select(self, x: int, y: int) -> None:
        # if the cursor is on the board
        if (
            x >= self.x_padd
            and x <= self.x_padd + self.board_size
            and y >= self.y_padd
            and y <= self.y_padd + self.board_size
        ):
            # find the row and col
            row = (y - self.y_padd) // self.cell_size
            col = (x - self.x_padd) // self.cell_size

            # highlight that square
            self.board.highlighted = [row, col]

    def switch(self, num: int | None) -> None:
        # if a square is highlighted
        if self.board.highlighted:
            row, col = self.board.highlighted

            # if that number isn't on the original board
            if self.board.original[row][col] is None:
                self.board.nums[row][col] = num

    def draw(self, screen: pygame.surface.Surface) -> None:
        # draw a white background
        screen.fill(WHITE)

        self.panel_start = self.x_padd + self.board_size + self.padd
        self.panel_width = self.cell_size * 2

        # panel border
        pygame.draw.rect(
            screen,
            BLACK,
            (self.panel_start, self.y_padd, self.panel_width, self.board_size),
            self.big_line_size,
        )

        # draw squares and numbers
        for row in range(9):
            for col in range(9):
                # get the colour of the square based on the status
                if [row, col] == self.board.highlighted:
                    colour = YELLOW
                elif self.board.original[row][col]:
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
                number = self.board.nums[row][col]

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
