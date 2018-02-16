from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True, error_messages={'unique': "A user with same email already exists!"})
    about_me = models.CharField('about me', max_length=150, blank=True)

