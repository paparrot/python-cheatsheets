class Point:
    color = 'red'
    circle = 2

    # Constructor
    # Execute when instance creating
    # Default values is 0
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y

    # Destructor
    # Execute before instance delete
    def __del__(self):
        print("Instance is deleting")


point = Point()
# Point is deleting here
