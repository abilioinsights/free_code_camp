import math

class R2Vector:
    """
    Class representing a 2D vector (x, y).
    """

    def __init__(self, *, x, y):
        """
        Initializes a 2D vector with components x and y.
        """
        if not all(isinstance(val, (int, float)) for val in (x, y)):
            raise TypeError("Vector components must be numbers (int or float).")
        self.x = x
        self.y = y

    def norm(self):
        """
        Returns the norm (magnitude) of the vector.
        """
        return math.sqrt(sum(val**2 for val in vars(self).values()))

    def normalize(self):
        """
        Returns a normalized vector (unit vector) in the same direction as the current vector.
        """
        norm = self.norm()
        if norm == 0:
            raise ValueError("Cannot normalize a vector with zero norm.")
        return self.__class__(**{i: getattr(self, i) / norm for i in vars(self)})

    def angle(self, other):
        """
        Returns the angle (in radians) between the current vector and another vector.
        """
        if type(self) != type(other):
            raise TypeError("Vectors must be of the same class.")
        dot_product = self * other
        norm_product = self.norm() * other.norm()
        if norm_product == 0:
            raise ValueError("Cannot calculate the angle with a vector of zero norm.")
        return math.acos(dot_product / norm_product)

    def __str__(self):
        return str(tuple(getattr(self, i) for i in vars(self)))

    def __repr__(self):
        arg_list = [f'{key}={val}' for key, val in vars(self).items()]
        args = ', '.join(arg_list)
        return f'{self.__class__.__name__}({args})'

    def __add__(self, other):
        if type(self) != type(other):
            return NotImplemented
        kwargs = {i: getattr(self, i) + getattr(other, i) for i in vars(self)}
        return self.__class__(**kwargs)

    def __sub__(self, other):
        if type(self) != type(other):
            return NotImplemented
        kwargs = {i: getattr(self, i) - getattr(other, i) for i in vars(self)}
        return self.__class__(**kwargs)

    def __mul__(self, other):
        if type(other) in (int, float):
            kwargs = {i: getattr(self, i) * other for i in vars(self)}
            return self.__class__(**kwargs)        
        elif type(self) == type(other):
            args = [getattr(self, i) * getattr(other, i) for i in vars(self)]
            return sum(args)            
        return NotImplemented

    def __eq__(self, other):
        if type(self) != type(other):
            return NotImplemented
        return all(getattr(self, i) == getattr(other, i) for i in vars(self))
        
    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if type(self) != type(other):
            return NotImplemented
        return self.norm() < other.norm()

    def __gt__(self, other):
        if type(self) != type(other):
            return NotImplemented
        return self.norm() > other.norm()

    def __le__(self, other):
        return not self > other

    def __ge__(self, other):
        return not self < other


class R3Vector(R2Vector):
    """
    Class representing a 3D vector (x, y, z), inheriting from R2Vector.
    """

    def __init__(self, *, x, y, z):
        """
        Initializes a 3D vector with components x, y, and z.
        """
        super().__init__(x=x, y=y)
        if not isinstance(z, (int, float)):
            raise TypeError("The z component must be a number (int or float).")
        self.z = z

    def cross(self, other):
        """
        Returns the cross product between the current vector and another vector.
        """
        if type(self) != type(other):
            return NotImplemented
        kwargs = {
            'x': self.y * other.z - self.z * other.y,
            'y': self.z * other.x - self.x * other.z,
            'z': self.x * other.y - self.y * other.x
        }
        return self.__class__(**kwargs)


class RNVector:
    """
    Class representing an n-dimensional vector.
    """

    def __init__(self, *components):
        """
        Initializes an n-dimensional vector with the provided components.
        """
        if not all(isinstance(val, (int, float)) for val in components):
            raise TypeError("All vector components must be numbers (int or float).")
        self.components = components

    def norm(self):
        """
        Returns the norm (magnitude) of the vector.
        """
        return math.sqrt(sum(val**2 for val in self.components))

    def normalize(self):
        """
        Returns a normalized vector (unit vector) in the same direction as the current vector.
        """
        norm = self.norm()
        if norm == 0:
            raise ValueError("Cannot normalize a vector with zero norm.")
        return self.__class__(*(val / norm for val in self.components))

    def angle(self, other):
        """
        Returns the angle (in radians) between the current vector and another vector.
        """
        if type(self) != type(other):
            raise TypeError("Vectors must be of the same class.")
        dot_product = self * other
        norm_product = self.norm() * other.norm()
        if norm_product == 0:
            raise ValueError("Cannot calculate the angle with a vector of zero norm.")
        return math.acos(dot_product / norm_product)

    def __str__(self):
        return str(self.components)

    def __repr__(self):
        arg_list = [f'{val}' for val in self.components]
        args = ', '.join(arg_list)
        return f'{self.__class__.__name__}({args})'

    def __add__(self, other):
        if type(self) != type(other):
            return NotImplemented
        return self.__class__(*(a + b for a, b in zip(self.components, other.components)))

    def __sub__(self, other):
        if type(self) != type(other):
            return NotImplemented
        return self.__class__(*(a - b for a, b in zip(self.components, other.components)))

    def __mul__(self, other):
        if type(other) in (int, float):
            return self.__class__(*(val * other for val in self.components))
        elif type(self) == type(other):
            return sum(a * b for a, b in zip(self.components, other.components))
        return NotImplemented

    def __eq__(self, other):
        if type(self) != type(other):
            return NotImplemented
        return all(a == b for a, b in zip(self.components, other.components))

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if type(self) != type(other):
            return NotImplemented
        return self.norm() < other.norm()

    def __gt__(self, other):
        if type(self) != type(other):
            return NotImplemented
        return self.norm() > other.norm()

    def __le__(self, other):
        return not self > other

    def __ge__(self, other):
        return not self < other


# Example usage
v1 = R3Vector(x=2, y=3, z=1)
v2 = R3Vector(x=0.5, y=1.25, z=2)
print(f'v1 = {v1}')
print(f'v2 = {v2}')
v3 = v1 + v2
print(f'v1 + v2 = {v3}')
v4 = v1 - v2
print(f'v1 - v2 = {v4}')
v5 = v1 * v2
print(f'v1 * v2 = {v5}')
v6 = v1.cross(v2)
print(f'v1 x v2 = {v6}')

# Example with RNVector
v7 = RNVector(1, 2, 3, 4)
v8 = RNVector(2, 3, 4, 5)
print(f'v7 = {v7}')
print(f'v8 = {v8}')
v9 = v7 + v8
print(f'v7 + v8 = {v9}')
v10 = v7 * v8
print(f'v7 * v8 = {v10}')
