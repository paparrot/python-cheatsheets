# Class
class Cat:
    # Class doc description
    """Class for manipulating with cats"""

    # Default public property value
    voice = 'Meow'

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

# Get all class properties
print(Cat.__dict__)

# Get class description
print(Cat.__doc__)

# Check instance/class has property
print(hasattr(cat1, 'voice'))
print(hasattr(Cat, 'voice'))

# Get instance/class property value
print(getattr(cat1, 'voice'))
print(getattr(Cat, 'voice'))

# Set instance/class property value (set value to instances, if used to class)
setattr(Cat, 'voice', 'Nice to meet you!')
print(getattr(Cat, 'voice'))

# If cat1 has no property "voice", it will be searching in class properties
print(getattr(cat1,'voice'))

# Delete property
delattr(Cat, 'voice')
if hasattr(Cat, 'voice'):
    print(getattr(Cat, 'voice'))

# Get instance property value
print(cat1.name)

# Set instance property value
cat1.name = 'Max'
print(cat1.name)
