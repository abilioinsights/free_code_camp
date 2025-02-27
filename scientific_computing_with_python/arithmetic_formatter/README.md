# Arithmetic Formatter

A Python function that takes a list of arithmetic problems (addition and subtraction) and formats them neatly in columns, adhering to specific rules.

## Features

- Supports addition (`+`) and subtraction (`-`) problems.
- Ensures proper formatting with numbers right-aligned and results displayed under the dashes.
- Displays up to 5 problems at a time.
- Optionally shows the answers to the problems.

## Requirements

- Python 3.x

## Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/arithmetic_formatter.git
cd arithmetic_formatter
```

## Usage
<p>Import the arithmetic_arranger function and pass a list of arithmetic problems to it.</p>

```py
from arithmetic_arranger import arithmetic_arranger

# List of problems to format
problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

# Call the function with or without showing the answers
print(arithmetic_arranger(problems, show_answers=True))
```

## Example Output
```diff
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
  730      3799      88      172
```
## Error Handling:
- Too many problems: If more than 5 problems are provided, the function will return ``Error: Too many problems``.
- Invalid operator: The function only supports + and -. Any other operators will return ``Error: Operator must be '+' or '-'``.
- Invalid numbers: If any of the numbers contain non-digit characters, the function will return ``Error: Numbers must only contain digits``.
- Number length: If any of the numbers are more than four digits long, the function will return ``Error: Numbers cannot be more than four digits``.

## Contributing
<p> Feel free to open issues or submit pull requests for improvements or bug fixes.</p>

## License
<p>This project is licensed under the MIT License. See the LICENSE file for more details.</p>
