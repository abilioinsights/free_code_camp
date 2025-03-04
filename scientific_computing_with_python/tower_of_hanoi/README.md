## Tower of Hanoi Solver
This Python project is an iterative solver for the Tower of Hanoi puzzle. The Tower of Hanoi is a mathematical puzzle that consists of three rods and a number of disks of different sizes. The goal is to move all the disks from the source rod to the target rod following these rules:

- Only one disk can be moved at a time.
- Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or an empty rod.
- No disk may be placed on a smaller disk.
The script allows the user to input the number of disks, and it displays each move required to solve the puzzle. The total number of moves needed is also shown.

## Features
- Iterative solution to the Tower of Hanoi puzzle.
- Displays each move in real time.
- Calculates the total number of moves required to solve the puzzle.
- Allows the user to input the number of disks.

## Usage
<ol>
<li>Clone this repository.</li>
<li>Run the script with Python.</li>
<li>Enter the number of disks to solve the puzzle.</li>
</ol>

```py
$ python hanoi_solver.py
Enter the number of disks: 3
```

## Example Output:

```py
Enter the number of disks (or type 0 to exit):  3

Total moves needed: 7

Move 1:
Source (A): [3, 2]
Auxiliary (B): []
Target (C): [1]


Move 2:
Source (A): [3]
Auxiliary (B): [2]
Target (C): [1]


Move 3:
Source (A): [3]
Auxiliary (B): [2, 1]
Target (C): []


Move 4:
Source (A): []
Auxiliary (B): [2, 1]
Target (C): [3]


Move 5:
Source (A): [1]
Auxiliary (B): [2]
Target (C): [3]


Move 6:
Source (A): [1]
Auxiliary (B): []
Target (C): [3, 2]


Move 7:
Source (A): []
Auxiliary (B): []
Target (C): [3, 2, 1]

```

## How it works
- The script calculates the total number of moves required using the formula 2^n - 1, where n is the number of disks.
- The moves are calculated iteratively and displayed step by step.

## Requirements
Python 3.x

## License
This project is open-source and free to use under the MIT License.
