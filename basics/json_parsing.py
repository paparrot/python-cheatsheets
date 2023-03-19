# JSON is commonly used with data APIS. Here is how we can parse JSON into Python dictionary.
import json

# Sample JSON
user_json = '{"name": "John", "last_name": "Doe", "age": 30}'

# Parse to dict
user = json.loads(user_json)
print(type(user))
print(user)

# Stringify
car = {'make': 'Ford', 'model': 'Mustang'}
print(json.dumps(car))
print(type(json.dumps(car)))

# Read JSON from file
with open('file.json') as file:
    json_content = json.load(file)
print(type(json_content))
print(json_content)
