# Sudoku Solver / Resolvedor de Sudoku

This Python script solves a Sudoku puzzle using backtracking. It includes methods to validate numbers in rows, columns, and squares.

Este script Python resolve um quebra-cabeça Sudoku usando backtracking. Ele inclui métodos para validar números em linhas, colunas e quadrantes.

## Features / Funcionalidades
- Solves Sudoku puzzles using backtracking. / Resolve quebra-cabeças Sudoku usando backtracking.
- Validates numbers in rows, columns, and squares. / Valida números em linhas, colunas e quadrantes.
- Displays the initial and solved puzzles. / Exibe o quebra-cabeça inicial e resolvido.

## How to Use / Como Usar
Define your Sudoku puzzle as a 9x9 list of lists, where empty cells are represented by 0. Then, call the `solve_sudoku` function with the puzzle.

Defina seu quebra-cabeça Sudoku como uma lista de listas 9x9, onde células vazias são representadas por 0. Em seguida, chame a função `solve_sudoku` com o quebra-cabeça.

### Example / Exemplo
```python
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

solve_sudoku(puzzle)
