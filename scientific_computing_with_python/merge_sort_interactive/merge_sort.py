def merge_sort(array):
    """Ordena uma lista usando o algoritmo Merge Sort."""
    if len(array) <= 1:
        return
    
    middle_point = len(array) // 2
    left_part = array[:middle_point]
    right_part = array[middle_point:]

    merge_sort(left_part)
    merge_sort(right_part)

    left_array_index = 0
    right_array_index = 0
    sorted_index = 0

    while left_array_index < len(left_part) and right_array_index < len(right_part):
        if left_part[left_array_index] < right_part[right_array_index]:
            array[sorted_index] = left_part[left_array_index]
            left_array_index += 1
        else:
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1
        sorted_index += 1

    while left_array_index < len(left_part):
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1
    
    while right_array_index < len(right_part):
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1

def is_valid_number_list(input_str):
    """
    Checks if the input string contains only valid numbers (integers).
    Returns True if valid, False otherwise.
    """
    try:
        list(map(int, input_str.split()))
        return True
    except ValueError:
        return False

def get_user_input():
    """Prompts the user for a list of numbers and validates the input."""
    user_numbers = input('Enter a list of numbers separated by spaces: ').strip()
    while not is_valid_number_list(user_numbers):
        print("Invalid input. Please enter a valid list of numbers (e.g., '3 5 1 2').")
        user_numbers = input('Enter a list of numbers separated by spaces: ').strip()
    return list(map(int, user_numbers.split()))

def main():
    # Default list of numbers
    default_numbers = [4, 10, 6, 14, 2, 1, 8, 5]
    
    # Ask if the user wants to input their own list
    user_input = input('Do you want to enter your own list of numbers? (y/n): \n').strip().lower()
    
    if user_input == 'y':
        numbers = get_user_input()
    else:
        numbers = default_numbers

    print('\nUnsorted array: ')
    print(numbers)
    
    merge_sort(numbers)
    
    print('\nSorted array: ')
    print(numbers)

if __name__ == '__main__':
    main()
