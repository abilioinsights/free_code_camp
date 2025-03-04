# Merge Sort Interactive

This project implements the Merge Sort algorithm in Python. It includes an interactive feature that allows the user to either sort a default list of numbers or input their own list. Additionally, the program validates user input to ensure only numbers are provided.

## Features

- **Merge Sort Algorithm**: Efficient sorting algorithm with O(n log n) time complexity.
- **Interactive Input**: Users can input their own list of numbers or use the default list.
- **Input Validation**: Ensures only valid numeric input is processed by checking that each element entered is a number.

## Input Validation

The program includes a validation method to ensure that only numeric values are entered. If a non-numeric value is detected, the program will notify the user and prompt for valid input again. This prevents errors and ensures the merge sort works with a clean list of integers.

### Example of invalid input:

```py
Enter a list of numbers separated by spaces: 3 a 5 Invalid input: please enter numbers only.
```


## How to Use

1. Run the Python script `merge_sort.py`.
2. The program will prompt:

```py
Do you want to enter your own list of numbers? (y/n):

- Type `y` to input your own list of numbers.
- Type `n` to use the default list: `[4, 10, 6, 14, 2, 1, 8, 5]`.
```

## 3. If you chose to input your own list, you will be asked to provide the numbers separated by spaces. Example:

```py
Enter a list of numbers separated by spaces: 3 9 2 7 5
````

## 4. The program will display the unsorted array, sort it using Merge Sort, and then display the sorted array.

```bash
## Example

```bash
Unsorted array: 
[4, 10, 6, 14, 2, 1, 8, 5]

Sorted array: 
[1, 2, 4, 5, 6, 8, 10, 14]
```

## How to Run
Make sure you have Python installed. You can run the program from the terminal or command line:

```py
python merge_sort.py
```

## License
This project is licensed under the MIT License.
