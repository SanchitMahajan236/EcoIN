from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserDetails(AbstractUser):
    # Username, Email and Password are automatically stored.
    desc = models.CharField(max_length=255,default="A EcoIn user")
