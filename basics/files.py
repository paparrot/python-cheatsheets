# Python has functions for creating, reading, updating, deleting files.
# Available modes:
# 'r' - read (default)
# 'w' - writing. Creates a new file if it doesn't exist or truncates the file if it exists.
# 'x' - exclusive creation. If the file already exists, the operation fails.
# 'a' - append. Creates a new file if it doesn't exist.
# '+' - modifier for basic modes, means updating the file. For example, 'r+' or 'w+'.
# 't' - text mode (default).
# 'b' - binary mode (commonly used for images).
# Also, you can mix modes, for example 'r+b' will read and write in binary mode.

# Open file with "write" mode
file = open('file.txt', 'w')

# Get some info
print(f'Name: {file.name}')
print(f'Closed: {file.closed}')
print(f'Mode: {file.mode}')

# Write to file
file.write('I love Python')
file.write(' and Javascript')
file.close()

# Append to file
file = open('file.txt', 'a')
file.write('\nAnd PHP!')
file.close()

# Set variable value from file
file = open('file.txt', 'r')
variable = file.read()
print(variable)

# Good practice is using context manager 'with' instead of manually opening and closing files
# File will close automatically after using context manager
with open('file.txt', 'r') as file:
    content = file.read()
    print(content)
