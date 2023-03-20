# A List is collection which is ordered and changeable. Allows duplicate members.

# Create list
nums = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']
# any type can be stored here
mix = ['a', 123, {'name': 'Ford'}]

# Use a constructor
# numbers = list(1,2,3,4) # Not common

# Use a generator
# Create a list of numbers from 1 to 14
print([i for i in range(1, 15)])

# Also you can add conditions to generators
print([i for i in range(1, 15) if i != 5])

# Get a value
print(fruits[1])

# Get a length
print(len(fruits))

# Append to list
fruits.append('Mangos')
print(fruits)

# Remove from list
fruits.remove("Grapes")
print(fruits)

# Insert into position
fruits.insert(2, 'Strawberries')
print(fruits)

# Change value
fruits[0] = "Blueberries"
print(fruits)

# Remove with pop (By position)
fruits.pop(2)
print(fruits)

# Reverse list
fruits.reverse()
print(fruits)

# Sort list
fruits.sort()
print(fruits)

# Reverse sort
fruits.sort(reverse=True)
print(fruits)

# Slice list
# It`s some kind of filters, but with simple syntax.
# syntax is some_list[START:STOP:STEP]

# Whole list
print(fruits[:])
print(fruits[::])

# Odd in order
print(fruits[::2])

# Even in order
print(fruits[1::2])

# Reverse list
print(fruits[::-1])

# All from 2
print(fruits[2:])

# All before 3
print(fruits[:3])
