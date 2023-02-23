# Class
class Cat:
    # Constructor
    def __init__(self, breed, age, name):
        # Setting values to class (public) properties
        self.breed = breed
        self.age = age
        self.name = name

    # Class method
    def draw(self):
        print(f'This is {self.name}. It is {self.breed}, {self.age} y.o.')


# Initializing class objects
cat1 = Cat('red', 1, 'Bob')
cat2 = Cat('black', 2, 'Marsik')

# Call instance method
cat2.draw()
cat1.draw()

# Get instance property
print(cat1.name)
