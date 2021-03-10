import re

from rest_framework import serializers
from user_management.exceptions import (
    InvalidNameException, InvalidPhoneException,
    InvalidPasswordLengthException,
)

def name_validator(value):
    try:
        if not value.isalpha():
            raise InvalidNameException(value)    
        
        return value
    
    except:
        raise InvalidNameException(value)


def phone_validator(value):
    try:
        if not value.isnumeric():
            raise InvalidPhoneException(value)
        
        return value
    
    except:
        raise InvalidPhoneException(value)


def password_validator(value): 
    if len(value) < 8:
        raise InvalidPasswordLengthException(value)

    return value