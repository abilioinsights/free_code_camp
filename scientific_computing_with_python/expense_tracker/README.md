# Expense Tracker

This Python project is a simple **Expense Tracker** application that allows users to add, view, and filter their expenses by category. It also calculates the total expenses for the user. The project is run in the terminal and accepts user input through a menu-based system.

## Features

- **Add an Expense**: Users can input the amount and category for their expenses.
- **List All Expenses**: Displays all the recorded expenses, showing both amount and category.
- **Show Total Expenses**: Calculates the total sum of all expenses entered.
- **Filter Expenses by Category**: Filters and displays expenses based on a specific category.
- **Exit**: Closes the program when the user is finished.

## Prerequisites

- **Python 3.x**: Make sure you have Python installed to run this project. You can download it from [here](https://www.python.org/downloads/).

## Usage

1. Clone the repository or download the `expense_manager.py` file into your local machine.
2. Open a terminal and navigate to the folder containing `expense_manager.py`.
3. Run the following command to start the expense tracker:

    ```bash
    python expense_manager.py
    ```

4. Follow the on-screen instructions to:
   - Add expenses
   - List all expenses
   - View the total expenses
   - Filter expenses by category
   - Exit the program

## Functions Overview

- `add_expense(expenses, amount, category)`: Adds an expense entry to the `expenses` list.
- `print_expenses(expenses)`: Prints all the expenses in a readable format.
- `total_expenses(expenses)`: Calculates and returns the total amount of expenses.
- `filter_expenses_by_category(expenses, category)`: Filters and returns expenses for a specific category.
- `main()`: The main program that runs the menu and handles user interaction.

## License

This project is free to use and modify. Feel free to customize it for your needs.
