# Sudoku Solver in Python

A Python program to solve Sudoku puzzles using backtracking. This project demonstrates the use of recursion, backtracking, and problem-solving skills to solve Sudoku puzzles efficiently.

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

This project is a Python implementation of a Sudoku solver. It uses a backtracking algorithm to find the correct solution for any valid Sudoku puzzle. The program checks the validity of numbers in rows, columns, and 3x3 squares, ensuring that the solution adheres to Sudoku rules.

---

## Features

- **Backtracking Algorithm**: Efficiently solves Sudoku puzzles using recursion and backtracking.
- **Input Validation**: Ensures the Sudoku puzzle is valid before attempting to solve it.
- **User-Friendly Output**: Displays the puzzle in a readable format, with empty cells represented by `*`.
- **Customizable**: Can be easily extended to include additional features like puzzle generation or a graphical interface.

---

## How It Works

The solver works as follows:
1. **Find Empty Cells**: The program searches for the first empty cell (represented by `0`) in the Sudoku grid.
2. **Validate Numbers**: For each empty cell, it checks if a number (1-9) is valid in the corresponding row, column, and 3x3 square.
3. **Backtracking**: If a number is valid, it places the number in the cell and recursively attempts to solve the rest of the puzzle. If the number leads to a dead end, it backtracks and tries the next number.
4. **Solution**: Once all cells are filled correctly, the puzzle is solved.

---

## Installation

## 1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/sudoku-solver.git
   ```

## 2. Navigate to the project directory:

```bash
cd sudoku-solver
```

## 3. Ensure you have Python installed (version 3.6 or higher).

## Usage
<ol>
  <li>Open the sudoku_solver.py file.</li>
  <li>Modify the puzzle variable to input your Sudoku puzzle. Use 0 to represent empty cells.</li>
  <li>Run the script:</li>
</ol>

```bash
python sudoku_solver.py
```

## Example - Input Puzzle
```bash
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
```

## Output
```bash

Puzzle to solve:
* * 2 * * 8 * * *
* * * * * 3 7 6 2
4 3 * * * * 8 * *
* 5 * * 3 * * 9 *
* 4 * * * * * 2 6
* * * 4 6 7 * * *
* 8 6 7 * 4 * * *
* * * 5 1 9 * * 8
1 7 * * * 6 * * 5

Solved puzzle:
6 1 2 9 5 8 3 4 7
9 8 5 1 4 3 7 6 2
4 3 7 6 2 5 8 1 9
2 5 8 6 3 1 4 9 7
3 4 1 8 9 2 5 7 6
7 9 5 4 6 3 1 8 2
5 8 6 7 2 4 9 3 1
7 2 3 5 1 9 6 4 8
1 7 4 3 8 6 2 5 9
```

## Contributing
Contributions are welcome! If you'd like to contribute, please follow these steps:

- Fork the repository.

- Create a new branch for your feature or bugfix.

- Make your changes and commit them.

- Submit a pull request with a detailed description of your changes.

## License
This project is licensed under the MIT License. See the LICENSE file for details
