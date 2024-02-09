from sudoku import Sudoku


class Board:
    def __init__(self, difficulty=0.5) -> None:
        self.original = Sudoku(3).difficulty(difficulty).board
        self.nums = [row.copy() for row in self.original]
        self.status = [[None for _ in range(9)] for _ in range(9)]
        self.highlighted = None

    def move_highlight(self, direction: str) -> None:
        if self.highlighted:
            # move the highlighted one left
            if direction == "left":
                if not self.highlighted[1] == 0:
                    self.highlighted[1] -= 1

            # move the highlighted one right
            elif direction == "right":
                if not self.highlighted[1] == 8:
                    self.highlighted[1] += 1

            # move the highlighted one up
            elif direction == "up":
                if not self.highlighted[0] == 0:
                    self.highlighted[0] -= 1

            # move the highlighted one down
            elif direction == "down":
                if not self.highlighted[0] == 8:
                    self.highlighted[0] += 1
