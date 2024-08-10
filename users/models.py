from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    image = models.ImageField(upload_to='profile_image', blank=True, null=True, verbose_name='Аватарка')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'
        db_table = 'users'
