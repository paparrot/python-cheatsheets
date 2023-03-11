class Vector:
    # Class properties
    MIN_COORD = 0
    MAX_COORD = 100

    # Method validate can use class properties MIN_COORD and MAX_COORD,
    # Class methods hasn't accessed to instance properties
    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    # Constructor
    def __init__(self, x, y):
        self.x = self.y = 0

        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

    # Default class method has accessed to class properties and instance properties
    def get_coord(self):
        return self.x, self.y

    # Static methods use for operations related to class subject
    # Static method hasn't accessed to class properties or instance properties
    @staticmethod
    def norm2(x, y):
        return x * x + y * y


v = Vector(1, 2)
res = v.get_coord()
print(res)  # return (1, 2)

print(Vector.validate(5))  # return True

v2 = Vector(200, 1)
res2 = v2.get_coord()
print(res2)  # return (0, 0)

print(Vector.norm2(4, 5))  # return 41
