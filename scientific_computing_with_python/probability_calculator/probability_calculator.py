import random

class Hat:
    def __init__(self, **balls):
        """Initialize the Hat with a given number of colored balls."""
        if not balls:
            raise ValueError("The hat must contain at least one ball.")

        self.contents = []
        for color, count in balls.items():
            if count < 1:
                raise ValueError(f"Each color must have at least one ball. Invalid count for {color}.")
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        """Draw a specified number of balls from the hat."""
        num_balls = min(num_balls, len(self.contents))  # Limit to available balls
        drawn_balls = random.sample(self.contents, num_balls)

        for ball in drawn_balls:
            self.contents.remove(ball)

        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """
    Perform multiple experiments to estimate the probability of drawing the expected balls.
    """
    successful_experiments = 0

    for _ in range(num_experiments):
        hat_copy = Hat(**{color: hat.contents.count(color) for color in set(hat.contents)})
        drawn_balls = hat_copy.draw(num_balls_drawn)
        drawn_counts = {color: drawn_balls.count(color) for color in set(drawn_balls)}

        if all(drawn_counts.get(color, 0) >= count for color, count in expected_balls.items()):
            successful_experiments += 1

    return (successful_experiments / num_experiments) * 100

def parse_input_dict(input_string):
    """Convert user input from 'color1=num1, color2=num2' format into a dictionary."""
    try:
        if input_string.strip().lower() == "exit":
            return "exit"
        
        items = input_string.split(",")
        parsed_dict = {}
        for item in items:
            color, num = item.strip().split("=")
            num = int(num)
            if num < 1:
                raise ValueError
            parsed_dict[color.strip()] = num
        return parsed_dict
    except (ValueError, IndexError):
        print("⚠ Invalid format! Please enter values like: blue=5, red=3")
        return None

def get_positive_integer(prompt):
    """Get a positive integer input from the user."""
    while True:
        value = input(prompt).strip().lower()
        if value == "exit":
            return "exit"
        try:
            value = int(value)
            if value < 1:
                raise ValueError
            return value
        except ValueError:
            print("⚠ Please enter a valid positive integer!")

def main():
    """Main function to handle user interaction."""
    print("🎩 Welcome to the Probability Calculator! 🎲")
    
    while True:  # Loop infinito até o usuário decidir sair
        mode = input("Do you want to\n(1) use default test \n(2) enter custom values? \n(1/2 or 'exit' to quit): ").strip().lower()
        if mode == "exit":
            print("👋 Exiting program. Goodbye!")
            break
        if mode in ("1", "2"):
            break
        print("⚠ Invalid choice! Please enter 1 or 2.")

    if mode == "exit":
        return
    
    if mode == "1":
        print("\nRunning default test case...\n")
        hat = Hat(blue=5, red=4, green=2)
        expected_balls = {'red': 1, 'green': 1}
        num_balls_drawn = 4
        num_experiments = 2000
    else:
        print("\nYou selected to input custom values.\n")

        while True:
            hat_input = input("Enter the number of balls for each color (e.g., blue=5, red=4, green=2) or type 'exit':\n ")
            if hat_input.lower() == "exit":
                print("👋 Exiting program. Goodbye!")
                return
            hat_dict = parse_input_dict(hat_input)
            if hat_dict and hat_dict != "exit":
                break

        while True:
            expected_input = input("\nEnter the expected balls you want to draw (e.g., red=2, green=1) or type 'exit':\n ")
            if expected_input.lower() == "exit":
                print("👋 Exiting program. Goodbye!")
                return
            expected_dict = parse_input_dict(expected_input)
            if expected_dict and expected_dict != "exit":
                break

        num_balls_drawn = get_positive_integer("\nEnter the number of balls to draw or type 'exit':\n ")
        if num_balls_drawn == "exit":
            print("👋 Exiting program. Goodbye!")
            return
        
        num_experiments = get_positive_integer("Enter the number of experiments to run or type 'exit': ")
        if num_experiments == "exit":
            print("👋 Exiting program. Goodbye!")
            return
        
        hat = Hat(**hat_dict)
        expected_balls = expected_dict
    
    probability = experiment(hat, expected_balls, num_balls_drawn, num_experiments)
    print(f"\n🎯 The estimated probability of drawing the expected balls: {probability:.2f}%\n")
    
    while True:
        restart = input("Do you want to run another experiment? (yes/no): ").strip().lower()
        if restart == "no":
            print("\n👋 Exiting program. Goodbye!")
            break
        elif restart == "yes":
            main()
            break
        else:
            print("⚠ Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()
