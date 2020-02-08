from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class CustomUserExtraField(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(blank=False, null=False)
    phoneNumber = models.PositiveIntegerField()
    postalCode = models.PositiveIntegerField()

    Bio = models.TextField(null=True, blank=True, default="Bio")
