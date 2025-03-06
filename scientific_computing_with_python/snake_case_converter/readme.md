# PascalCase/CamelCase to Snake_Case Converter

A simple Python utility to convert strings written in PascalCase or CamelCase into snake_case. This is useful for developers working with naming conventions across different programming languages or APIs that require different case formats.

## Features

- Converts PascalCase and CamelCase strings to snake_case.
- Supports converting full words while handling uppercase characters.
- Ignores and retains non-alphabetic characters like spaces or punctuation.

## Installation

Clone this repository:

```bash
git clone https://github.com/YOUR_USERNAME/snake_case_converter.git
cd snake_case_converter
```
No external dependencies are required; this project runs on Python's built-in features.

## Usage
To use the converter, you can simply call the convert_to_snake_case function, passing a PascalCase or CamelCase string as an argument.

<h3>Example usage:</h3>

```py
from snake_case_converter import convert_to_snake_case

# Convert a PascalCase or CamelCase string to snake_case
snake_case_string = convert_to_snake_case('ThisIsCamelCase')
print(snake_case_string)  # Output: this_is_camel_case
```

<h2>Running the Script</h2>
<p>Alternatively, you can run the converter directly from the command line by adding a main() function:</p>

```py
if __name__ == "__main__":
    print(convert_to_snake_case("MyPascalCasedString"))
```
<h2>How It Works</h2>
The converter iterates through the input string, checks for uppercase characters, converts them to lowercase, and prepends an underscore (_) before each one. Lowercase characters remain unchanged. The final result is returned as a snake_cased string with leading underscores stripped, if necessary.

<h2 style="text-align: center;">Pascal/CamelCase to Snake_Case Conversion</h2>

 | Pascal/CamelCase           | Snake_Case           |
|----------------------------|----------------------|
| `ThisIsPascalCase`          | `this_is_pascal_case`|
| `convertThisToSnakeCase`    | `convert_this_to_snake_case` |
| `SnakeCase`                 | `snake_case`         |
