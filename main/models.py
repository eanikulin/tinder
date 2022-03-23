from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4


class User(AbstractUser):
    MALE, FEMALE = 'M', 'W'
    GENDER_CHOICES = ((MALE, 'М'), (FEMALE, 'Ж'),)

    uid = models.UUIDField(primary_key=True, default=uuid4)
    first_name = models.CharField(verbose_name='Имя', max_length=50)
    last_name = models.CharField(verbose_name='Фамилия', max_length=50)
    email = models.EmailField(verbose_name='Электронная почта', unique=True)
    gender = models.CharField(verbose_name='пол', max_length=1, choices=GENDER_CHOICES, blank=True)
    image = models.ImageField(upload_to='users_images', blank=True, null=True)

    def __str__(self):
        return self.last_name + " " + self.first_name

    class Meta:
        ordering = ('-pk',)
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'
