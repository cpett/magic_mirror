from django.db import models
from django.contrib.auth.models import AbstractUser

# Define models here
class User(AbstractUser):
    # Inherited from AbstractUser and AbstractBaseUser
    # password
    # last_login
    # first_name
    # last_name
    # email
    # is_staff
    # help_text
    # is_active
    # date_joined
    city = models.TextField(max_length=30, null=True, blank=True)
    state = models.TextField(max_length=30, null=True, blank=True)
    country = models.TextField(max_length=30, null=True, blank=True)
    zip = models.TextField(max_length=30, null=True, blank=True)
