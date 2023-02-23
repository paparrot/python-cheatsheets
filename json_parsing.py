# JSON is commonly used with data APIS. Here is how we can parse JSON into Python dictionary.
import json

# Sample JSON
user_json = '{"name": "John", "last_name": "Doe", "age": 30}'

# Parse to dict
user = json.loads(user_json)
print(user)

# Stringify
car = {'make': 'Ford', 'model': 'Mustang'}
print(json.dumps(car))
print(type(json.dumps(car)))
