class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    # This method will create new property in class instance,
    # Not in class
    def set_min_coord(self, min_val):
        self.MIN_COORD = min_val

    # Right way to set class properties
    @classmethod
    def set_min(cls, min_val):
        cls.MIN_COORD = min_val

    # Call every time when trying to get property from instance
    # We can use it for manage getters behaviour
    def __getattribute__(self, item):
        print("__getattribute__")
        # Hide property x
        if item == 'x':
            pass
        else:
            return object.__getattribute__(self, item)

    # Call every time when trying to set property to instance
    def __setattr__(self, key, value):
        print("__setattr__")
        if key == 'x':
            pass
        else:
            object.__setattr__(self, key, value)

    # Call every time when trying to get property from instance that not exists
    def __getattr__(self, item):
        print('__getattr__', item)

    def __delattr__(self, item):
        print("__delattr__", item)
        object.__delattr__(self, item)


pt = Point(1, 15)  # Call __setattr__ two times

print(pt.test)  # return None and  call __getattr__

pt.set_min_coord(20)  # Call __getattribute__, __setattr__
print(pt.MIN_COORD)  # return 20 and call __getattribute__

print(Point.MIN_COORD)  # return 0

Point.set_min(30)
print(Point.MIN_COORD)  # return 30

del pt.y  # Delete property x and call __delattr__
print(pt.y)  # Call __getattribute__ and __getattr__
