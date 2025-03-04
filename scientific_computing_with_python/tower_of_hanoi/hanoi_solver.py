def hanoi_iterative(n, source, auxiliary, target):
    rods = {
        'A': list(range(n, 0, -1)),  # The source rod
        'B': [],  # The auxiliary rod
        'C': []   # The target rod
    }
    total_moves = 2 ** n - 1
    print(f"\nTotal moves needed: {total_moves}")
    
    for move_num in range(1, total_moves + 1):
        if move_num % 3 == 1:
            move_disk(rods, 'A', 'C', n)  # Move between source and target
        elif move_num % 3 == 2:
            move_disk(rods, 'A', 'B', n)  # Move between source and auxiliary
        elif move_num % 3 == 0:
            move_disk(rods, 'B', 'C', n)  # Move between auxiliary and target

        # Display the progress after each move
        print(f"\nMove {move_num}:")
        print(f"Source (A): {rods['A']}")
        print(f"Auxiliary (B): {rods['B']}")
        print(f"Target (C): {rods['C']}\n")

def move_disk(rods, source, target, n):
    if not rods[target]:  # Target rod is empty, move disk from source
        rods[target].append(rods[source].pop())
    elif not rods[source]:  # Source rod is empty, move disk from target
        rods[source].append(rods[target].pop())
    elif rods[source][-1] < rods[target][-1]:  # Move from source to target
        rods[target].append(rods[source].pop())
    else:  # Move from target to source
        rods[source].append(rods[target].pop())

# Main loop
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
