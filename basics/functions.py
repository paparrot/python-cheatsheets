# A function is a block of code which only runs when it`s called.
# In Python, we do not use curly brackets, we use indentation with tabs or spaces

# Create function
def say_hello(name: str) -> None:
    print(f'Hello, {name}')


def get_sum(num1: int, num2: int) -> int:
    return num1 + num2


# Functions can also take arguments from user input, you can also add hints to them
def hello_custom_name(name: str) -> None:
    print(f'Hello, {name}')


say_hello("John Doe")
hello_custom_name(input("Enter your name: "))
print(get_sum(3, 4))

# Lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# Very similar to js arrow functions
get_sum_second = lambda num1, num2: num1 + num2  # NOQA - disable code quality warning for this row
print(get_sum_second(12, 14))
