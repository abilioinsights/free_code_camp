def initialize_rods(n):
    """Initialize the rods with disks on the source rod."""
    return {
        'A': list(range(n, 0, -1)),  # Source rod
        'B': [],  # Auxiliary rod
        'C': []   # Target rod
    }

def move_disk(rods, source, target):
    """
    Move a disk between two rods.
    :param rods: Dictionary containing the rods.
    :param source: Source rod.
    :param target: Target rod.
    """
    if not rods[target]:  # Target rod is empty, move disk from source
        rods[target].append(rods[source].pop())
    elif not rods[source]:  # Source rod is empty, move disk from target
        rods[source].append(rods[target].pop())
    elif rods[source][-1] < rods[target][-1]:  # Move from source to target
        rods[target].append(rods[source].pop())
    else:  # Move from target to source
        rods[source].append(rods[target].pop())

def hanoi_iterative(n, source, auxiliary, target):
    """
    Solve the Towers of Hanoi problem iteratively.
    :param n: Number of disks.
    :param source: Source rod.
    :param auxiliary: Auxiliary rod.
    :param target: Target rod.
    """
    rods = initialize_rods(n)
    total_moves = 2 ** n - 1
    print(f"\nTotal moves needed: {total_moves}")
    
    for move_num in range(1, total_moves + 1):
        if move_num % 3 == 1:
            move_disk(rods, source, target)  # Move between source and target rods
        elif move_num % 3 == 2:
            move_disk(rods, source, auxiliary)  # Move between source and auxiliary rods
        elif move_num % 3 == 0:
            move_disk(rods, auxiliary, target)  # Move between auxiliary and target rods

        # Display the progress after each move
        print(f"\nMove {move_num}:")
        print(f"Source ({source}): {rods[source]}")
        print(f"Auxiliary ({auxiliary}): {rods[auxiliary]}")
        print(f"Target ({target}): {rods[target]}\n")

def main():
    """Main function to run the Hanoi solver."""
    while True:
        try:
            num_disks = int(input("Enter the number of disks (or type 0 to exit): "))
            if num_disks == 0:
                break
            elif num_disks < 0:
                print("Please enter a positive number of disks.")
            else:
                hanoi_iterative(num_disks, 'A', 'B', 'C')
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == '__main__':
    main()
