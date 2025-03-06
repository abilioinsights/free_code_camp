def handle_edge_cases(square_target):
    """Handles edge cases for 0 and 1."""
    if square_target == 1:
        print(f'The square root of {square_target} is 1')
        return 1
    elif square_target == 0:
        print(f'The square root of {square_target} is 0')
        return 0
    return None

def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    """Calculates the square root of a number using the bisection method."""
    # Check if the target is negative
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    
    # Handle edge cases for 0 and 1
    root = handle_edge_cases(square_target)
    if root is not None:
        return root

    # Set the initial bounds for the bisection method
    low = 0
    high = max(1, square_target)
    root = None

    # Perform bisection search
    for _ in range(max_iterations):
        mid = (low + high) / 2
        square_mid = mid**2

        # Check if the current estimate is within the tolerance
        if abs(square_mid - square_target) < tolerance:
            root = mid
            break

        # Adjust bounds based on the comparison
        elif square_mid < square_target:
            low = mid
        else:
            high = mid

    # If no root is found after max_iterations
    if root is None:
        print(f"Failed to converge within {max_iterations} iterations.")
    else:   
        print(f'The square root of {square_target} is approximately {root}')

    return root

def main():
    """Main function to handle user input and output."""
    try:
        N = float(input("Enter a number to find its square root: "))
        square_root_bisection(N)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
