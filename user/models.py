from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# This is first way to extend your user model..
# .. as you don't need to change User model fields but you want to add some information
# no change in user auth
# .
# .
# .
class CustomUserExtraField(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(blank=False, null=False)
    phoneNumber = models.PositiveIntegerField()
    postalCode = models.PositiveIntegerField()
    Bio = models.TextField(null=True, blank=True, default="Bio")
    # profileImage = models.ImageField(null=True, blank=True)
    # https://medium.com/@frfahim/django-registration-with-confirmation-email-bb5da011e4ef
    # should use this for send confirmation email
    # https://pypi.org/project/django-phone-verify/
