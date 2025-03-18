from abc import ABC, abstractmethod
import re


class Equation(ABC):
    """Abstract base class for mathematical equations."""
    
    degree: int
    type: str

    def __init__(self, *args):
        """Initializes the equation with given coefficients, ensuring correctness."""
        if (self.degree + 1) != len(args):
            raise TypeError(
                f"'Equation' object takes {self.degree + 1} positional arguments but {len(args)} were given"
            )
        if any(not isinstance(arg, (int, float)) for arg in args):
            raise TypeError("Coefficients must be of type 'int' or 'float'")
        if args[0] == 0:
            raise ValueError("Highest degree coefficient must be different from zero")
        self.coefficients = {(len(args) - n - 1): arg for n, arg in enumerate(args)}

    def __init_subclass__(cls):
        """Ensures subclasses define required attributes."""
        if not hasattr(cls, "degree"):
            raise AttributeError(
                f"Cannot create '{cls.__name__}' class: missing required attribute 'degree'"
            )
        if not hasattr(cls, "type"):
            raise AttributeError(
                f"Cannot create '{cls.__name__}' class: missing required attribute 'type'"
            )

    def __str__(self):
        """Returns a formatted string representation of the equation."""
        terms = []
        for n, coefficient in self.coefficients.items():
            if not coefficient:
                continue
            sign = '+' if coefficient > 0 else ''
            
            # Remover .0 se o número for um inteiro
            coefficient_str = f'{sign}{coefficient:.1f}'.rstrip('0').rstrip('.')
            
            if n == 0:
                terms.append(coefficient_str)
            elif n == 1:
                terms.append(f'{coefficient_str}x')
            else:
                terms.append(f"{coefficient_str}x^{n}")
    
        equation_string = ' '.join(terms) + ' = 0'
        equation_string = re.sub(r"(?<!\d)1(?=x)", "", equation_string.strip("+"))  # Remover coeficiente 1 de x
        return equation_string.replace('x^2', 'x²')


    

    @abstractmethod
    def solve(self):
        """Abstract method for solving the equation."""
        pass

    @abstractmethod
    def analyze(self):
        """Abstract method for analyzing the equation."""
        pass


class LinearEquation(Equation):
    """Represents a linear equation of the form ax + b = 0."""
    
    degree = 1
    type = 'Linear Equation'

    def solve(self):
        """Solves the linear equation."""
        a, b = self.coefficients.values()
        x = -b / a
        return [x]

    def analyze(self):
        """Returns the slope and y-intercept of the equation."""
        slope, intercept = self.coefficients.values()
        return {'slope': slope, 'intercept': intercept}


class QuadraticEquation(Equation):
    """Represents a quadratic equation of the form ax^2 + bx + c = 0."""
    
    degree = 2
    type = 'Quadratic Equation'

    def __init__(self, *args):
        """Initializes the quadratic equation and calculates the discriminant."""
        super().__init__(*args)
        a, b, c = self.coefficients.values()
        self.delta = b**2 - 4 * a * c

    def solve(self):
        """Solves the quadratic equation."""
        if self.delta < 0:
            return []
        a, b, _ = self.coefficients.values()
        x1 = (-b + (self.delta) ** 0.5) / (2 * a)
        x2 = (-b - (self.delta) ** 0.5) / (2 * a)
        return [x1] if self.delta == 0 else [x1, x2]

    def analyze(self):
        """Analyzes the quadratic function, returning vertex and concavity."""
        a, b, c = self.coefficients.values()
        x = -b / (2 * a)
        y = a * x**2 + b * x + c
        concavity = 'upwards' if a > 0 else 'downwards'
        min_max = 'min' if a > 0 else 'max'
        return {'x': x, 'y': y, 'min_max': min_max, 'concavity': concavity}


def solver(equation):
    """Solves and analyzes a given equation, returning formatted results."""
    
    if not isinstance(equation, Equation):
        raise TypeError("Argument must be an Equation object")

    output_string = f'\n{equation.type:-^24}'
    output_string += f'\n\n{equation!s:^24}\n\n'
    output_string += f'{"Solutions":-^24}\n\n'
    
    results = equation.solve()
    match results:
        case []:
            result_list = ['No real roots']
        case [x]:
            result_list = [f'x = {x:+.3f}']
        case [x1, x2]:
            result_list = [f'x₁ = {x1:+.3f}', f'x₂ = {x2:+.3f}']

    for result in result_list:
        output_string += f'{result:^24}\n'

    output_string += f'\n{"Details":-^24}\n\n'
    details = equation.analyze()

    match details:
        case {'slope': slope, 'intercept': intercept}:
            details_list = [f'Slope = {slope:>16.3f}', f'Y-intercept = {intercept:>10.3f}']
        case {'x': x, 'y': y, 'min_max': min_max, 'concavity': concavity}:
            coord = f'({x:.3f}, {y:.3f})'
            details_list = [f'Concavity = {concavity: >12}', f'{min_max.capitalize()} = {coord: >18}']

    for detail in details_list:
        output_string += f'{detail}\n'
    
    return output_string


def get_numeric_input(prompt):
    """Gets a numeric input from the user, ensuring valid input."""
    
    while True:
        user_input = input(prompt).strip()
        if user_input.lower() == 'exit':
            return None
        try:
            return float(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    """Main loop for user interaction, allowing multiple equation inputs."""
    
    print("\nEquation Solver - Type 'exit' to quit at any time.\n")

    while True:
        print("\nChoose the equation type:\n1. Linear (ax + b = 0)\n2. Quadratic (ax² + bx + c = 0)")
        choice = input("Enter 1 or 2: ").strip()

        if choice.lower() == 'exit':
            print("\nExiting Equation Solver. Goodbye!\n")
            break
        if choice not in ['1', '2']:
            print("Invalid choice. Please enter 1 or 2.")
            continue

        # Get coefficients with validation
        if choice == '1':
            print("\nEnter coefficients for a linear equation (ax + b = 0):")
            a = get_numeric_input("Enter the value of a: ")
            if a is None: break
            b = get_numeric_input("Enter the value of b: ")
            if b is None: break
            try:
                equation = LinearEquation(a, b)
            except (TypeError, ValueError) as e:
                print(f"Error: {e}")
                continue

        else:
            print("\nEnter coefficients for a quadratic equation (ax² + bx + c = 0):")
            a = get_numeric_input("Enter the value of a: ")
            if a is None: break
            b = get_numeric_input("Enter the value of b: ")
            if b is None: break
            c = get_numeric_input("Enter the value of c: ")
            if c is None: break
            try:
                equation = QuadraticEquation(a, b, c)
            except (TypeError, ValueError) as e:
                print(f"Error: {e}")
                continue

        print(solver(equation))


if __name__ == "__main__":
    main()
