# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create tuple
fruits = ('Apples', 'Oranges', 'Grapes')
# fruits = tuple(('Apples', 'Oranges', 'Grapes')) // Uncommon
# fruits = ('Apple',) // Single value need trailing comma
print(type(fruits))
print(fruits[1])

# Can't change items !!!
# fruits[0] = 'Pears'

# Delete tuple
del fruits
# prints(fruits) // Not found

# Set is a collection which is unordered and unindexed. No duplicate methods.

# Create set
fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if in set
print('Apples' in fruits_set)
print(fruits_set)

# Add to set
fruits_set.add('Grapes')
print(fruits_set)

# Add duplicate
fruits_set.add("Apples")
print(fruits_set)

# Remove from set
fruits_set.remove('Grapes')
print(fruits_set)

# Clear set
fruits_set.clear()
print(fruits_set)

del fruits_set
# print(fruits_set) // Not found
