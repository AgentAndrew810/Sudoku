import pygame
from board import Board
from constants import BLACK, WHITE, BLUE, YELLOW, PADDING


class Game:
    def __init__(self, screen: pygame.surface.Surface) -> None:
        self.active = True
        self.board = Board()
        self.set_sizes(screen.get_size())

    def set_sizes(self, size: tuple[int, int]) -> None:
        # get the full width and height of the screen
        self.full_width, self.full_height = size

        # set the panel width to 1/6 of the width
        self.panel_width = 1 / 6 * self.full_width

        # calculate the available width and height, by removing padding and panel width
        available_width = self.full_width - PADDING * 3 - self.panel_width
        available_height = self.full_height - PADDING * 2

        # set default values of padding
        self.x_padd = PADDING
        self.y_padd = PADDING

        if available_width > available_height:
            # if the available width is greater than the height, calculate cell_size from height, add more x padd
            self.cell_size = available_height // 9
            self.x_padd += (available_width - available_height) // 3
        else:
            # if the available height is greater than the width, calculate cell_size from width, add more y padd
            self.cell_size = available_width // 9
            self.y_padd += (available_height - available_width) // 2

        # based on the cell_size calculate the fontsize
        fontsize = int(self.cell_size * 42 / 62)
        self.font = pygame.font.SysFont(None, fontsize)

        # calculate helper values (not required but simplify code)
        self.big_cell_size = self.cell_size * 3
        self.board_size = self.cell_size * 9
        self.panel_start = self.x_padd + self.board_size + self.x_padd

    def x_coord(self, x):
        return self.x_padd + x * self.cell_size

    def y_coord(self, y):
        return self.y_padd + y * self.cell_size

    def select(self, x: int, y: int) -> None:
        # if the cursor is on the board
        if (
            x >= self.x_padd
            and x <= self.x_padd + self.board_size
            and y >= self.y_padd
            and y <= self.y_padd + self.board_size
        ):
            # find the row and col
            row = int((y - self.y_padd) // self.cell_size)
            col = int((x - self.x_padd) // self.cell_size)

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

        # panel border
        pygame.draw.rect(screen, BLACK, (self.panel_start, self.y_padd, self.panel_width, self.board_size), 5)

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

                pygame.draw.rect(screen, colour, (self.x_coord(col), self.y_coord(row), self.cell_size, self.cell_size))

                # get the number on that square
                number = self.board.nums[row][col]

                # if there is a number draw it on the square
                if number:
                    width, height = self.font.size(str(number))
                    font_surf = self.font.render(str(number), True, BLACK)
                    screen.blit(font_surf, (self.x_coord(col + 0.5) - width // 2, self.y_coord(row + 0.5) - height // 2))

        # draw inside lines
        for i in range(10):
            # vertical lines
            pygame.draw.line(screen, BLACK, (self.x_coord(i), self.y_padd), (self.x_coord(i), self.y_padd + self.board_size))
            # horizontal lines
            pygame.draw.line(screen, BLACK, (self.x_padd, self.y_coord(i)), (self.x_padd + self.board_size, self.y_coord(i)))

        # draw outside lines
        for i in range(4):
            # vertical lines
            pygame.draw.line(
                screen,
                BLACK,
                (self.x_padd + self.big_cell_size * i, self.y_padd),
                (self.x_padd + self.big_cell_size * i, self.y_padd + self.board_size),
                5,
            )
            # horizontal lines
            pygame.draw.line(
                screen,
                BLACK,
                (self.x_padd, self.y_padd + self.big_cell_size * i),
                (self.x_padd + self.board_size, self.y_padd + self.big_cell_size * i),
                5,
            )
