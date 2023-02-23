# A module is basically a file containing a set of functions to include in your application.
# There are core python modules, modules you can install the pip package manager
# (including Django) as well as custom modules

# Core modules
from time import time
from datetime import date

# Pip modules
from camelcase import CamelCase

# Custom modules
from validator import validate_email

email = "example@mail.ru"
if validate_email(email):
    print(f'Email {email} is valid')

c = CamelCase()
print(c.hump('Hello there world'))

# today = datetime.date.today()
today = date.today()
timestamp = time()

print(timestamp)
print(today)
