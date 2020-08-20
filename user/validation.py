from django.core.exceptions import ValidationError
import re

def validate_phone(value):

    regex = re.compile(r'(\d{3}).*(\d{4}).*(\d{4})')

    if not regex.match(value):
        raise ValidationError(message = 00)

def validate_email(value):

    regex = re.compile(r'^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$')

    if not regex.match(value):
        raise ValidationError(message = 11)

def validate_account(value):

    regex = re.compile(r'^[a-zA-Z0-9]{4,16}$')

    if not regex.match(value):
        raise ValidationError(message = 22)

def validate_birthday(value):

    regex = re.compile(r'^[0-9]{8}')

    if not regex.match(value):
        raise ValidationError(message = 33)
        
def validate_name(value):

    regex = re.compile(r'^[가-힣a-zA-Z]+$')

    if not regex.match(value):
        raise ValidationError(message = 44)