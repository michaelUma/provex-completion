from django.db import models

# Create your models here.
# login/models.py

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Add any additional fields you want here
    # For example, you can add fields like 'profile_picture' or 'date_of_birth'.
    pass
