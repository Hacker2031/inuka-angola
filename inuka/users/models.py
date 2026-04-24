from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    TIPO_USUARIO = [
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
    ]
    tipo_usuario = models.CharField(max_length=20, choices = TIPO_USUARIO, default='a')
    categoria = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        db_table="users"
        verbose_name='User'
        verbose_name_plural='Users'
