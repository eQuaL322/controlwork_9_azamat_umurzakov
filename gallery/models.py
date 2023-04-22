from django.contrib.auth import get_user_model
from django.db import models

from accounts.models import UserProfile


class Photo(models.Model):
    image = models.ImageField(
        verbose_name='Фотография',
        null=False,
        blank=True,
        upload_to='photos',
    )
    caption = models.TextField(
        verbose_name='Подпись',
        max_length=1000,
        null=False,
        blank=False,
    )
    created_at = models.DateTimeField(
        verbose_name='Дата и время создания',
        auto_now_add=True,
    )
    author = models.ForeignKey(
        verbose_name='Автор',
        to=get_user_model(),
        related_name='author',
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['-created_at']


class Favorite(models.Model):
    user = models.ForeignKey(
        to=UserProfile,
        related_name='favorite_user',
        verbose_name='Избранноое',
        null=False,
        on_delete=models.CASCADE
    )
    photo = models.ForeignKey(
        to=Photo,
        related_name='favorites',
        related_query_name='favorite',
        verbose_name='Избранноое',
        null=False,
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('user', 'photo')
