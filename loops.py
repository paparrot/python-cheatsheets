# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set or a string)

people = ['John', 'Paul', 'Sara', 'Susan']

# Simple for loop
for person in people:
    print(f'Current person')

print('---')

# Break
for person in people:
    if person == 'Sara':
        break
    print(f'Peson is {person}')

print('---')

# Continue
for person in people:
    if person == 'Sara':
        continue
    print(f'Peson is {person}')

print('---')

# Range
for i in range(len(people)):
    print(people[i])

print('---')

for i in range(0, 10):
    print(i)

print('---')

# While loops execute a set of statements as long as a condition is true.

count = 0
while count < 10:
    print(count)
    count += 1
