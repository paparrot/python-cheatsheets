# A dictionary is a collection which is unordered, changeable and indexed. No duplicate members

# Create dict
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
}
print(person)
print(type(person))

# Use a constructor
person2 = dict(first_name="John", last_name="Doe")
print(person2)

# Get value
print(person['first_name'])  # If key don`t exists raise KeyError
print(person.get('first_name'))  # If key don`t exists return None

# Add key/value
person['phone'] = '88005553535'
print(person.get('phone'))

# Get dict keys, return set-like object
print(person.keys())

# Get dict items, return set-like object
print(person.items())

# Copy dict
next_person = person.copy()
print(next_person)

next_person['phone'] = '8909302010'
print(person)
print(next_person)

# Remove item
del (person['age'])
person.pop('phone')
print(person)

# Clear
person.clear()
print(person)

# Length
print(len(next_person))

# List of dicts
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Max', 'age': 25},
]

# Get name value from second dict
print(people[1]['name'])
