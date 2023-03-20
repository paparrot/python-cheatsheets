# A module is basically a file containing a set of functions to include in your application.
# There are core python modules, modules you can install the pip package manager
# (including Django) as well as custom modules

# Good practice is:
# import first whole module (import modulename)
# after 1 blank line import part of module (from modulename import part)
# after 1 blank line import your custom modules (import mymodule)
# after 1 blank line import part of your module (from mymodule import part)


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
