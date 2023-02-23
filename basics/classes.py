# A class is like blueprint for creating objects. An object has properties and methods (functions) associated with it.
# Almost everything in Python is an object.

# Create class
class User:
    # Constructor
    def __init__(self, name: str, email: str, age: int):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age += 1


# Extends class
class Customer(User):
    # Constructor
    def __init__(self, name: str, email: str, age: int, balance: int):
        super().__init__(name, email, age)
        self._balance = balance

    def get_balance(self):
        return self._balance


# Init user object
me = User('Klim Subbotin', 'subbotin.klim@gmail.com', 27)
print(type(me))
print(me.greeting())
me.has_birthday()
print(me.greeting())

# Init customer object
customer = Customer('John Doe', 'johndoe@mail.ru', 30, 20)
print(customer.greeting())
print(customer.get_balance())