# Square Root Bisection Method

This project implements the square root calculation using the **Bisection Method** in Python. The Bisection Method is a numerical technique to approximate solutions of equations, and here it's applied to find the square root of a given number with a certain tolerance.

## Features

- Calculates the square root of a number using the Bisection Method.
- Handles edge cases for numbers 0 and 1.
- Validates input to avoid square roots of negative numbers (which are not defined in real numbers).
- Configurable tolerance and maximum number of iterations.
- Asks the user for input, making it interactive.

## Usage

### Requirements

Ensure you have Python 3.x installed. No external dependencies are required for this project.

### Running the Program

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/square-root-bisection.git
    cd square-root-bisection
    ```

2. Run the Python script:

    ```bash
    python square_root_bisection.py
    ```

3. Enter the number for which you want to calculate the square root:

    ```bash
    Enter a number to find its square root:
    ```

4. The program will then return the square root approximation based on the bisection method.

### Example

Input:

```bash
Enter a number to find its square root: 16
```
<p>The square root of 16 is approximately 4.0
</p>

## Configuration
<p>You can customize the following parameters within the square_root_bisection function:</p>
<ul>
<li>tolerance: The acceptable error in the result (default is 1e-7).</li>
<li>max_iterations: The maximum number of iterations allowed for the method to converge (default is 100).</li>
  </ul>
### Example of a customized call:

```py
square_root_bisection(16, tolerance=1e-5, max_iterations=50)
```

## Error Handling
<p>If you attempt to calculate the square root of a negative number, a ValueError will be raised, as the square root of negative numbers is not defined in real numbers.</p>
<p>Example:</p>

```bash
ValueError: Square root of negative number is not defined in real numbers
```

## Contributing
<p>Contributions are welcome! Please open an issue or submit a pull request for any improvements or new features.</p>
