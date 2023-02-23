# If / Else conditions are used to decide to do something based on something being true or false

x = 10
y = 5

# Comparison Operators (==, !=, >, <, >=, <=) – Used to compare values
if x > y:
    print(f'{x} is greater than {y}')
elif x == y:
    print(f'{x} is equals to {y}')
else:
    print(f'{y} is greater than {x}')

# Nested if
# if x > 2:
#     if x <= 10:
#         print(f'{x} is greater than 2 and less than or equal to 10')


# Logical operators (and, or, not) – Used to combine conditional statements
# x > 2 and x <= 10
if 2 < x <= 10:
    print(f'{x} is greater than 2 and less than or equal to 10')

if 2 < x or x <= 10:
    print(f'{x} is greater than 2 and less than or equal to 10')

if not (x == y):
    print(f'{x} is not {y}')

# Membership operator (not, not in) – Used to test if a sequence is presented in an object
numbers = [1, 2, 3, 4]

if x in numbers:
    print(f'{x} in numbers')

if x not in numbers:
    print(f'{x} is not in numbers')

# Identity operators (is, is not) – Compare the objects, not if they are equal,
# but if they are actually the same object, with the same memory location
x = 20
y = 20

if x is y:
    print(f'{x} is {y}')
