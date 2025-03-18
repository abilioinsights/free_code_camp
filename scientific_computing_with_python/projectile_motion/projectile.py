import math 

# Constants for physics calculations and graph representation
GRAVITATIONAL_ACCELERATION = 9.81  # m/s²
PROJECTILE = "∙"  # Symbol for projectile in trajectory graph
X_AXIS_TICK = "T"  # Symbol for x-axis
Y_AXIS_TICK = "⊣"  # Symbol for y-axis

class Projectile:
    """
    Represents a projectile launched with an initial speed, height, and angle.

    Attributes:
        speed (float): Initial speed in m/s.
        height (float): Initial height in meters.
        angle (float): Launch angle in degrees.
        speed_unit (str): The unit used for speed (e.g., 'm/s', 'km/h', 'mph').
    """

    __slots__ = ('__speed', '__height', '__angle', '__speed_unit')

    def __init__(self, speed, height, angle, speed_unit="m/s"):
        self.__speed = speed
        self.__height = height
        self.__angle = math.radians(angle)  # Convert angle to radians
        self.__speed_unit = speed_unit

    def __str__(self):
        """
        Returns a formatted string representing the details of the projectile, including its speed in the chosen unit.
        """
        return f'''
Projectile details:
Speed: {self.display_speed()} {self.__speed_unit}
Height: {self.height} m
Angle: {self.angle}°
Displacement: {round(self.__calculate_displacement(), 1)} m
'''

    def display_speed(self):
        """
        Displays the speed in the unit selected by the user.
        
        Returns:
            float: The speed value in the selected unit.
        """
        if self.__speed_unit == "km/h":
            return self.__speed * 3.6  # Conversion factor from m/s to km/h
        elif self.__speed_unit == "mph":
            return self.__speed * 2.23694  # Conversion factor from m/s to mph
        return self.__speed  # Default is m/s

    def __calculate_displacement(self):
        """
        Computes the total horizontal displacement of the projectile.

        Returns:
            float: The total displacement in meters.
        """
        horizontal_component = self.__speed * math.cos(self.__angle)
        vertical_component = self.__speed * math.sin(self.__angle)
        squared_component = vertical_component**2
        gh_component = 2 * GRAVITATIONAL_ACCELERATION * self.__height
        sqrt_component = math.sqrt(squared_component + gh_component)
        
        return horizontal_component * (vertical_component + sqrt_component) / GRAVITATIONAL_ACCELERATION
        
    def __calculate_y_coordinate(self, x):
        """
        Computes the y-coordinate (height) of the projectile at a given x-coordinate.

        Args:
            x (float): The horizontal position.

        Returns:
            float: The corresponding height (y-coordinate).
        """
        height_component = self.__height
        angle_component = math.tan(self.__angle) * x
        acceleration_component = GRAVITATIONAL_ACCELERATION * x ** 2 / (
                2 * self.__speed ** 2 * math.cos(self.__angle) ** 2)
        return height_component + angle_component - acceleration_component
    
    def calculate_all_coordinates(self):
        """
        Generates a list of all (x, y) coordinates of the projectile's trajectory.

        Returns:
            list of tuples: A list containing (x, y) coordinates.
        """
        return [
            (x, self.__calculate_y_coordinate(x))
            for x in range(math.ceil(self.__calculate_displacement()))
        ]

    @property
    def height(self):
        return self.__height

    @property
    def angle(self):
        return round(math.degrees(self.__angle))

    @property
    def speed(self):
        return self.__speed

    @height.setter
    def height(self, n):
        self.__height = n

    @angle.setter
    def angle(self, n):
        self.__angle = math.radians(n)

    @speed.setter
    def speed(self, s):
       self.__speed = s
    
    def __repr__(self):
        return f'{self.__class__.__name__}({self.speed}, {self.height}, {self.angle})'

class Graph:
    """
    Represents a graphical visualization of a projectile's trajectory.

    Attributes:
        coordinates (list of tuples): List of (x, y) coordinates of the projectile path.
    """

    __slots__ = ('__coordinates')

    def __init__(self, coord):
        self.__coordinates = coord

    def __repr__(self):
        return f"Graph({self.__coordinates})"

    def create_coordinates_table(self):
        """
        Creates a formatted table displaying the projectile's trajectory data.

        Returns:
            str: The trajectory table as a string.
        """
        table = '\n  x      y\n'
        for x, y in self.__coordinates:
            table += f'{x:>3}{y:>7.2f}\n'
        return table

    def create_trajectory(self):
        """
        Creates an ASCII representation of the projectile's trajectory.

        Returns:
            str: The trajectory graph as a string.
        """
        rounded_coords = [(round(x), round(y)) for x, y in self.__coordinates]

        x_max = max(rounded_coords, key=lambda i: i[0])[0]
        y_max = max(rounded_coords, key=lambda j: j[1])[1]

        matrix_list = [[" " for _ in range(x_max + 1)] for _ in range(y_max + 1)]

        for x, y in rounded_coords:
            matrix_list[-1 - y][x] = PROJECTILE

        matrix = ["".join(line) for line in matrix_list]

        matrix_axes = [Y_AXIS_TICK + row for row in matrix]
        matrix_axes.append(" " + X_AXIS_TICK * (len(matrix[0])))

        return "\n" + "\n".join(matrix_axes) + "\n"

def projectile_helper(speed, height, angle, speed_unit="m/s"):
    """
    Runs a projectile simulation given user input parameters.

    Args:
        speed (float): The initial speed of the projectile.
        height (float): The initial height of the projectile.
        angle (float): The launch angle of the projectile.
        speed_unit (str): The unit used for speed (e.g., 'm/s', 'km/h', 'mph').
    """
    projectile = Projectile(speed, height, angle, speed_unit)
    coordinates = projectile.calculate_all_coordinates()
    graph = Graph(coordinates)

    print(projectile)
    print(graph.create_coordinates_table())
    print(graph.create_trajectory())

def main():
    """
    Main function to provide a user menu for simulating projectile motion.
    """
    while True:
        print("\n🚀 Projectile Motion Simulator 🚀")
        print("1. Run an example (Speed: 10m/s, Height: 3m, Angle: 45°)")
        print("2. Enter custom values")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            print("\nRunning example...\n")
            projectile_helper(10, 3, 45)

        elif choice == "2":
            # Ask for unit preference first
            print("\nSelect the speed unit:")
            print("1. Miles per hour (mph)")
            print("2. Meters per second (m/s)")
            print("3. Kilometers per hour (km/h)")
            unit_choice = input("Enter your choice (1/2/3): ")

            # Convert user input to desired units
            if unit_choice == "1":
                unit = "mph"
                factor = 0.44704  # Conversion factor from mph to m/s
            elif unit_choice == "2":
                unit = "m/s"
                factor = 1  # No conversion needed
            elif unit_choice == "3":
                unit = "km/h"
                factor = 0.277778  # Conversion factor from km/h to m/s
            else:
                print("\n❌ Invalid choice. Returning to the main menu...")
                continue

            try:
                speed = float(input(f"Enter speed ({unit}): ")) * factor
                height = float(input("Enter initial height (m): "))
                angle = float(input("Enter launch angle (degrees): "))

                if speed <= 0 or angle < 0 or angle > 90:
                    print("\n❌ Invalid input! Speed must be positive, and angle must be between 0° and 90°.")
                    continue

                print("\nRunning custom simulation...\n")
                projectile_helper(speed, height, angle, unit)

            except ValueError:
                print("\n❌ Invalid input! Please enter numerical values.")

        elif choice == "3":
            print("\nGoodbye! 🚀")
            break

        else:
            print("\n❌ Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
