from django.contrib.auth import get_user_model
from django.db import models


class UserProfile(models.Model):
    user_profile = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name='Профиль пользователя',
    )
    favorites = models.ManyToManyField(
        to='gallery.Photo',
        through='gallery.Favorite',
    )

    def __str__(self):
        return self.user_profile
