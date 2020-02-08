from django.core import validators
from django.utils.deconstruct import deconstructible


@deconstructible
class UserNameCustomUserValidator(validators.RegexValidator):
    regex = r'^[\w.@+-]+\Z'  # it says which characters can not used
    message = (
        'Enter a valid username. This value may contain only letters, '
        'numbers, and @/./+/-/_ characters.'

    )# you can add lazy
    flags = 0


@deconstructible
class NameCustomUserValidator(validators.RegexValidator):
    regex = r'^[a-zA-Z]+$'  # it says which characters can  used
    message = (
        'Enter a valid username. This value may contain only letters, '

    )# you can add lazy to translate
    flags = 0