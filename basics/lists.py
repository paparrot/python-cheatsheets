# A List is collections which is ordered and changeable. Allows duplicate members.

# Create list
nums = [1,2,3,4,5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']


# Use a constructor
# numbers = list(1,2,3,4) // Not common

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


