from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, AbstractUser
from django.db import models


class UserProfile(AbstractUser):
    favorites = models.ManyToManyField(
        to='gallery.Photo',
        through='gallery.Favorite',
    )
