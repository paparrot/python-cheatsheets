# Class
class Cat:
    # Constructor
    def __init__(self, breed, age, name):
        self.breed = breed
        self.age = age
        self.name = name

    def draw(self):
        print(f'This is {self.name}. He is {self.breed}, {self.age} y.o.')

cat1 = Cat('red', 1, 'Bob')
cat2 = Cat('black', 2, 'Marsik')

cat2.draw()
cat1.draw()

