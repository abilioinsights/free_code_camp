def merge_sort(array):
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
    This function checks if the input string contains only valid numbers (integers).
    Returns True if valid, False otherwise.
    """
    try:
        # Try converting each element to an integer
        list(map(int, input_str.split()))
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    # Default list of numbers
    default_numbers = [4, 10, 6, 14, 2, 1, 8, 5]
    
    # Ask if the user wants to input their own list
    user_input = input('Do you want to enter your own list of numbers? (y/n): \n').strip().lower()
    
    if user_input == 'y':
        user_numbers = input('Enter a list of numbers separated by spaces: ').strip()
        
        # Validate user input
        while not is_valid_number_list(user_numbers):
            print("Invalid input. Please enter a valid list of numbers.\n")
            user_numbers = input('Enter a list of numbers separated by spaces: ').strip()
        
        # Convert valid input to a list of integers
        numbers = list(map(int, user_numbers.split()))
    else:
        numbers = default_numbers

    print('\nUnsorted array: ')
    print(numbers)
    
    merge_sort(numbers)
    
    print('\nSorted array: ')
    print(numbers)
