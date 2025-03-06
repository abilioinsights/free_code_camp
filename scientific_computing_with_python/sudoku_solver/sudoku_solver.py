class Board:
    def __init__(self, board):
        """
        Initialize the Sudoku board.
        :param board: A 9x9 list of lists representing the Sudoku puzzle.
        """
        self.board = board

    def __str__(self):
        """
        Convert the Sudoku board to a human-readable string format.
        Empty cells (0) are represented by '*'.
        :return: A string representation of the board.
        """
        board_str = ''
        for row in self.board:
            row_str = [str(i) if i else '*' for i in row]  # Replace 0 with '*' for empty cells
            board_str += ' '.join(row_str) + '\n'  # Join row items with spaces and add a newline
        return board_str

    def find_empty_cell(self):
        """
        Find the first empty cell (cell with value 0) in the board.
        :return: A tuple (row, col) representing the position of the empty cell, or None if no empty cells are found.
        """
        for row, contents in enumerate(self.board):
            try:
                col = contents.index(0)  # Find the index of the first 0 in the row
                return row, col
            except ValueError:
                pass  # If no 0 is found in the row, continue to the next row
        return None  # Return None if no empty cells are found

    def valid_in_row(self, row, num):
        """
        Check if a number is valid in the given row.
        :param row: The row index to check.
        :param num: The number to validate.
        :return: True if the number is not in the row, False otherwise.
        """
        return num not in self.board[row]

    def valid_in_col(self, col, num):
        """
        Check if a number is valid in the given column.
        :param col: The column index to check.
        :param num: The number to validate.
        :return: True if the number is not in the column, False otherwise.
        """
        return all(self.board[row][col] != num for row in range(9))

    def valid_in_square(self, row, col, num):
        """
        Check if a number is valid in the 3x3 square containing the given cell.
        :param row: The row index of the cell.
        :param col: The column index of the cell.
        :param num: The number to validate.
        :return: True if the number is not in the square, False otherwise.
        """
        row_start = (row // 3) * 3  # Find the starting row of the 3x3 square
        col_start = (col // 3) * 3  # Find the starting column of the 3x3 square
        for r in range(row_start, row_start + 3):  # Iterate over the rows in the square
            for c in range(col_start, col_start + 3):  # Iterate over the columns in the square
                if self.board[r][c] == num:  # If the number is already in the square, return False
                    return False
        return True  # Return True if the number is not in the square

    def is_valid(self, empty, num):
        """
        Check if a number is valid in the given empty cell.
        :param empty: A tuple (row, col) representing the position of the empty cell.
        :param num: The number to validate.
        :return: True if the number is valid in the row, column, and square, False otherwise.
        """
        row, col = empty
        valid_in_row = self.valid_in_row(row, num)  # Check if the number is valid in the row
        valid_in_col = self.valid_in_col(col, num)  # Check if the number is valid in the column
        valid_in_square = self.valid_in_square(row, col, num)  # Check if the number is valid in the square
        return all([valid_in_row, valid_in_col, valid_in_square])  # Return True if all checks pass

    def solver(self):
        """
        Solve the Sudoku puzzle using backtracking.
        :return: True if the puzzle is solved, False otherwise.
        """
        if (next_empty := self.find_empty_cell()) is None:  # If no empty cells are found, the puzzle is solved
            return True
        for guess in range(1, 10):  # Try numbers from 1 to 9
            if self.is_valid(next_empty, guess):  # If the number is valid in the empty cell
                row, col = next_empty
                self.board[row][col] = guess  # Place the number in the cell
                if self.solver():  # Recursively solve the puzzle
                    return True
                self.board[row][col] = 0  # Backtrack: remove the number if it doesn't lead to a solution
        return False  # Return False if no number leads to a solution

def solve_sudoku(board):
    """
    Solve and display the Sudoku puzzle.
    :param board: A 9x9 list of lists representing the Sudoku puzzle.
    :return: The solved Sudoku board.
    """
    gameboard = Board(board)  # Create a Board instance
    print(f'Puzzle to solve:\n{gameboard}')  # Display the initial puzzle
    if gameboard.solver():  # Solve the puzzle
        print(f'Solved puzzle:\n{gameboard}')  # Display the solved puzzle
    else:
        print('The provided puzzle is unsolvable.')  # Display a message if the puzzle is unsolvable
    return gameboard

# Example Sudoku puzzle
puzzle = [
  [0, 0, 2, 0, 0, 8, 0, 0, 0],
  [0, 0, 0, 0, 0, 3, 7, 6, 2],
  [4, 3, 0, 0, 0, 0, 8, 0, 0],
  [0, 5, 0, 0, 3, 0, 0, 9, 0],
  [0, 4, 0, 0, 0, 0, 0, 2, 6],
  [0, 0, 0, 4, 6, 7, 0, 0, 0],
  [0, 8, 6, 7, 0, 4, 0, 0, 0],
  [0, 0, 0, 5, 1, 9, 0, 0, 8],
  [1, 7, 0, 0, 0, 6, 0, 0, 5]
]

# Solve the puzzle
solve_sudoku(puzzle)
