# Generated by Django 4.2 on 2023-04-22 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_alter_favorite_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', related_query_name='favorite', to='gallery.photo', verbose_name='Избранноое'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(blank=True, upload_to='photos', verbose_name='Фотография'),
        ),
    ]
