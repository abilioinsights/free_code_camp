class Rectangle:
    """
    A class to represent a rectangle.
    Attributes:
        width (int or float): The width of the rectangle.
        height (int or float): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes the rectangle with a given width and height.
        
        Parameters:
            width (int or float): The width of the rectangle.
            height (int or float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def set_width(self, width):
        """
        Sets the width of the rectangle.
        
        Parameters:
            width (int or float): The new width of the rectangle.
        """
        self.width = width

    def set_height(self, height):
        """
        Sets the height of the rectangle.
        
        Parameters:
            height (int or float): The new height of the rectangle.
        """
        self.height = height

    def get_area(self):
        """
        Returns the area of the rectangle.
        
        Returns:
            float: The area of the rectangle (width * height).
        """
        return self.width * self.height

    def get_perimeter(self):
        """
        Returns the perimeter of the rectangle.
        
        Returns:
            float: The perimeter of the rectangle (2 * width + 2 * height).
        """
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        """
        Returns the diagonal length of the rectangle.
        
        Returns:
            float: The diagonal length using the Pythagorean theorem (sqrt(width^2 + height^2)).
        """
        return (self.width**2 + self.height**2) ** 0.5

    def get_picture(self):
        """
        Returns a string representation of the rectangle using '*' characters.
        The number of lines will be equal to the height, and the number of '*' in each line 
        will be equal to the width. If either the width or height is greater than 50, 
        it returns 'Too big for picture.'
        
        Returns:
            str: The string representation of the rectangle or a message if too large.
        """
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        return ('*' * self.width + '\n') * self.height

    def get_amount_inside(self, shape):
        """
        Returns the number of times the given shape (Rectangle or Square) can fit inside the rectangle.
        
        Parameters:
            shape (Rectangle or Square): The shape to be fit inside the rectangle.
        
        Returns:
            int: The number of times the given shape can fit inside the rectangle (no rotations).
        """
        return (self.width // shape.width) * (self.height // shape.height)

    def __str__(self):
        """
        Returns the string representation of the rectangle.
        
        Returns:
            str: The string representation of the rectangle in the format:
                 'Rectangle(width=<width>, height=<height>)'
        """
        return f'Rectangle(width={self.width}, height={self.height})'


class Square(Rectangle):
    """
    A class to represent a square, which is a subclass of Rectangle.
    The square is initialized with a single side length, and the width and height are the same.
    """

    def __init__(self, side):
        """
        Initializes the square with a given side length. The width and height are set to the side length.
        
        Parameters:
            side (int or float): The length of one side of the square.
        """
        super().__init__(side, side)

    def set_side(self, side):
        """
        Sets the side length of the square. Since a square has equal width and height,
        both dimensions are updated.
        
        Parameters:
            side (int or float): The new side length of the square.
        """
        self.width = side
        self.height = side

    def set_width(self, width):
        """
        Sets the width of the square. Since a square has equal width and height,
        the height is also set to the same value as the width.
        
        Parameters:
            width (int or float): The new width of the square.
        """
        self.width = width
        self.height = width  # Ensure both width and height are the same

    def set_height(self, height):
        """
        Sets the height of the square. Since a square has equal width and height,
        the width is also set to the same value as the height.
        
        Parameters:
            height (int or float): The new height of the square.
        """
        self.height = height
        self.width = height  # Ensure both height and width are the same

    def __str__(self):
        """
        Returns the string representation of the square.
        
        Returns:
            str: The string representation of the square in the format:
                 'Square(side=<side>)'
        """
        return f'Square(side={self.width})'


# Example usage
rect = Rectangle(10, 5)
print(rect.get_area())  # Output: 50
rect.set_height(3)
print(rect.get_perimeter())  # Output: 26
print(rect)  # Output: Rectangle(width=10, height=3)
print(rect.get_picture())  # Output: A picture with width 10 and height 3

sq = Square(9)
print(sq.get_area())  # Output: 81
sq.set_side(4)
print(sq.get_diagonal())  # Output: 5.656854249492381
print(sq)  # Output: Square(side=4)
print(sq.get_picture())  # Output: A picture of a square with side 4

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))  # Output: 8
