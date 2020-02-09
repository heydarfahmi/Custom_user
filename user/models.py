from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User, PermissionsMixin
from django.db import models

# Create your models here.
# This is first way to extend your user model..
# .. as you don't need to change User model fields but you want to add some information
# no change in user auth
# .
# .
# .
# class CustomUserExtraField(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     address = models.TextField(blank=False, null=False)
#     phoneNumber = models.PositiveIntegerField()
#     postalCode = models.PositiveIntegerField()
#     Bio = models.TextField(null=True, blank=True, default="Bio")
#     # profileImage = models.ImageField(null=True, blank=True)
#     # https://medium.com/@frfahim/django-registration-with-confirmation-email-bb5da011e4ef
#     # should use this for send confirmation email
#     # https://pypi.org/project/django-phone-verify/
#this is first way to extend django user by some fields


# ### second way to customize User
#
#
from phonenumber_field.formfields import PhoneNumberField

from user.custom_validators import UserNameCustomUserValidator, NameCustomUserValidator

## AbstractBaseUser:
# Create your own user model by subclassing Django’s AbstractBaseUser.
# We need to add the unique=True parameter to whatever field we are using as the USERNAME_FIELD
# REQUIRED_FIELDS is a list of fields that will be mandatory to create a user.
# # Note that including the USERNAME_FIELD here will give you an error when you try to run your app.
# password doesn’t need to be added to the REQUIRED_FIELDS list.
##PERMISSIONMIXIN:
# PermissionsMixin; this is a really helpful model that provides you with the methods,
# you need to work with the Django permissions module with minimal pain and suffering
# #Note that we also need to add a get_short_name method,
# #as Django expects a short name to be available for each user. This can be whatever field you want.


# with out manager you wont be able to access to admin or add user
## You’ll need to define methods for create_user , create_superuser , and get_by_natural_key at a minimum, or you will encounter errors
##user.is_staff :this controls access to the admin site.
# user.is_superuser : when True, the user has all available permissions
# user.save() is saving the data from the form to the database
## The get_by_natural_key method  should be set to whatever the id credential will be, effectively the username , or whatever you’re replacing that value with — in our use case, this is email.

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, firstName, lastName, password):
        user = self.model(username=username, email=email, firstName=firstName, lastName=lastName)
        user.set_password(password)
        user.is_staff = False
        user.is_superuser = False
        user.save()
        return user

    def create_superuser(self, username, email, firstName, lastName, password):
        user = self.create_user(username=username, email=email, firstName=firstName, lastName=lastName,
                                password=password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, username):
        print(username)
        return self.get(username=username)
class CustomUser(AbstractBaseUser, PermissionsMixin):
    username_validator = UserNameCustomUserValidator()
    nameString_validator = NameCustomUserValidator()
    username = models.CharField(
        ('username'),
        max_length=150,
        unique=True,
        help_text=('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': ("A user with that username already exists."),
        },
    )
    M = "Male"
    F = "Female"
    genres = ((M, "Male"), (F, "Female"))
    phoneNumber = PhoneNumberField()
    homeCall = PhoneNumberField(blank=True, null=True)
    email = models.EmailField(unique=True, default="example@example.com", null=True)
    firstName = models.CharField(max_length=50, default='firstname')
    lastName = models.CharField(max_length=50, default='lastname')
    genre = models.CharField(max_length=20, choices=genres, default='Male')
    is_staff = models.BooleanField(default=False)
    REQUIRED_FIELDS = ['email', 'firstName', 'lastName']
    USERNAME_FIELD = 'username'

    objects = CustomUserManager()

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.username  # show in terminal or ...

    def natural_key(self):
        return self.username  # use as uniqe key
# customize user completed.

# # Create your models here.