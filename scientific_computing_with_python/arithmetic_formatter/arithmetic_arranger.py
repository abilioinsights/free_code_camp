def arithmetic_arranger(problems, show_answers=False):
    # Constants
    MAX_PROBLEMS = 5
    MAX_DIGITS = 4

    # Check if there are too many problems
    if len(problems) > MAX_PROBLEMS:
        return "Error: Too many problems."

    # Lists to store the formatted parts
    top_lines = []  # Stores the first line numbers
    bottom_lines = []  # Stores the operators and second numbers
    separators = []  # Stores the dashes ----
    results = []  # Stores the result of each operation

    for operation in problems:
        # Split the operation into operands and operator
        operand_first_line, operator_symbol, operand_second_line = operation.split()

        # Validate input
        error = validate_input(operand_first_line, operand_second_line, operator_symbol)
        if error:
            return error

        # Calculate the result of the operation
        result = calculate_result(operand_first_line, operand_second_line, operator_symbol)

        # Calculate the length needed for proper formatting
        length = max(len(operand_first_line), len(operand_second_line)) + 2

        # Format each part of the operation
        formatted_top_line = operand_first_line.rjust(length)
        formatted_bottom_lines = operator_symbol + operand_second_line.rjust(length - 1)
        formatted_separators = '-' * length
        formatted_result = result.rjust(length)

        # Add the formatted parts to their corresponding lists
        top_lines.append(formatted_top_line)
        bottom_lines.append(formatted_bottom_lines)
        separators.append(formatted_separators)
        results.append(formatted_result)

    # Join the formatted parts with four spaces between each problem
    arranged_problems = "    ".join(top_lines) + "\n" + "    ".join(bottom_lines) + "\n" + "    ".join(separators)
    
    # Add the results if 'show_answers' is True
    if show_answers:
        arranged_problems += "\n" + "    ".join(results)

    return arranged_problems


def validate_input(operand_first_line, operand_second_line, operator_symbol):
    """Valida a entrada do problema aritmético."""
    if operator_symbol not in ['+', '-']:
        return "Error: Operator must be '+' or '-'."
    if not (operand_first_line.isdigit() and operand_second_line.isdigit()):
        return "Error: Numbers must only contain digits."
    if len(operand_first_line) > 4 or len(operand_second_line) > 4:
        return "Error: Numbers cannot be more than four digits."
    return None


def calculate_result(operand_first_line, operand_second_line, operator_symbol):
    """Calcula o resultado da operação."""
    if operator_symbol == '+':
        return str(int(operand_first_line) + int(operand_second_line))
    else:
        return str(int(operand_first_line) - int(operand_second_line))

# Example usage
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], show_answers=True))
