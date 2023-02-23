# Python has functions for creating, reading, updating, deleting files.

# Open file with "write" mode
file = open('file.txt', 'w')

# Get some info
print(f'Name: {file.name}')
print(f'Name: {file.closed}')
print(f'Name: {file.mode}')

# Write to file
file.write('I love Python')
file.write(' and Javascript')
file.close()

# Append to file
file = open('file.txt', 'a')
file.write('\nAnd PHP!')
file.close()