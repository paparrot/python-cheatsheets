# A function is a block of code which only runs when its called.
# In Python, we do not use curly brackets, we use indentation with tabs or spaces

# Create function
def say_hello(name: str) -> None:
    print(f'Hello, {name}')


def get_sum(num1: int, num2: int) -> int:
    return num1 + num2


say_hello("John Doe")
print(get_sum(3, 4))

# Lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# Very similar to js arrow functions


get_sum_second = lambda num1, num2: num1 + num2
print(get_sum_second(12, 14))
