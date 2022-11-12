from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    

class Account(AbstractUser):
    SEX_CHOICES = [('M', 'мужской'), ('F', 'женский')] 
    name = models.CharField(max_length=150)
    role = models.ForeignKey('accounts.Role', verbose_name=('Роль'), on_delete=models.CASCADE, related_name='account', null=True)
    phone = models.CharField(max_length=20, verbose_name='Телефон', null=True)
    photo = models.ImageField(upload_to='photo', verbose_name='Фото', null=True)
    birthday = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    telegram = models.CharField(max_length=50, null=True)
    facebook = models.CharField(max_length=50, null=True)
    linkedin = models.CharField(max_length=50, null=True)

    sex = models.CharField(
        choices=SEX_CHOICES,
        null=True,
        blank=True,
        verbose_name='Пол',
        max_length=1
    )

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

