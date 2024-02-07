from sudoku import Sudoku

class Board:
    def __init__(self, difficulty=0.5) -> None:
        self.original = Sudoku(3).difficulty(difficulty).board
        self.nums = [row.copy() for row in self.starting_board]
        self.status = [[None for _ in range(9)] for _ in range(9)]
