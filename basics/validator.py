# This is example custom module to be imported to modules.py
import re


def validate_email(email: str) -> bool:
    if len(email) > 7:
        return bool(re.match('^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$',
                             email))
