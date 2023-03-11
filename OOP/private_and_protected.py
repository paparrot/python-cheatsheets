class Point:
    def __init__(self, x, y):
        # Public property
        # Access from everywhere
        self.x = x
        self.y = y


# We should use private properties when we don't want give access users
# pt = Point(1, 2)
# To change values manually
# pt.x = 200
# Or change values type manually
# pt.y = "coord_py"

class ProtectedPoint:
    def __init__(self, x, y):
        # Protected properties
        # Access from class and child classes
        self._x = x
        self._y = y


# Programmer CAN get and set protected properties manually
# But shouldn't. IDE will warn about this
# pt = ProtectedPoint(1, 2)
# print(pt._x)
# pt._x = 22
# print(pt._x)


class PrivatePoint:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    # Getter
    def get_x(self):
        return self.__x

    # We can get properties inside methods
    def get_y(self):
        return self.__y

    # Setter
    def set_x(self, x):
        if self.__check_value(x):
            self.__x = x

    # Validate values before set
    def set_y(self, y):
        if self.__check_value(y):
            self.__y = y

    # Private method
    @staticmethod
    def __check_value(val):
        return type(val) in (int, float)


pt = PrivatePoint(3, 10)
print(pt.get_x())  # return 3
pt.set_x(28)
print(pt.get_x())  # return 28
print(pt.__x)  # AttributeError
pt.__check_value(132)  # AttributeError

print(pt._PrivatePoint__x)  # return 28 😔
# This is highly not recommended example of getting private property value
# You can also use module for making private and protected properties and avoid this case
