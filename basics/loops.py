# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set or a string)

people = ['John', 'Paul', 'Sara', 'Susan']

# Simple for loop
for person in people:
    print(f'Current person')

print('---')

# Break (stop cycle if a condition occurs)
for person in people:
    if person == 'Sara':
        break
    print(f'Person is {person}')

print('---')

# Continue (skip current iteration if a condition occurs)
for person in people:
    if person == 'Sara':
        continue
    print(f'Person is {person}')

print('---')


# Range (look for length of target collection and set it as count of iterations)
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
