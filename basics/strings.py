# Strings
# They are iterable, so you can use them like lists or tuples

name = "Klim"
age = 27

# Concatenate
print('Hello, my name is ' + name + ' and I am ' + str(age))

# String Formatting

# Arguments by position (like Java, bad practice)
print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-strings (Best practice, but only python 3.6+)
print(f'Hello, my name is {name} and I am {age}')

# Strings Methods
s = 'hello world'

# String capitalizing / upper / lower / swap
print(s.capitalize())
print(s.upper())
print(s.lower())
print(s.swapcase())

# Length
print(len(s))

# Replace
print(s.replace('hello', 'goodbye'))
# Very useful while you need to replace specsymbols or spaces
print('Hello fellow kid$$$'.replace('$', '').replace(' ', ''))

# Count
sub = 'h'
print(s.count(sub))

# Starts with
print(s.startswith('hello'))

# Ends with 
print(s.endswith('world'))

# Split into a list
print(s.split())
# Split intp a list with separator
print('Hello mr.Bicycle!'.split('.'))

# Find position
print(s.find('r'))

# Is alphanumeric
print(s.isalnum())

# Is alphabetic
print('Rustam'.isalpha())

# Is all numeric
print(s.isnumeric())
