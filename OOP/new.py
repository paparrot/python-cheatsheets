class Point:
    # Magic method __new__
    # Execute before __init__
    # Should return result of parent method __new__ with cls argument for creating new instance
    def __new__(cls, *args, **kwargs):
        print("I am execute before instance created")
        return super().__new__(cls)

    def __init__(self):
        self.x = 0
        print("I am execute after instance created")


p = Point()
