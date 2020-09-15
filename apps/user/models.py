from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    username = models.CharField(max_length=50, verbose_name='用户名')
    nikename = models.CharField(max_length=50, verbose_name='昵称')
    email = models.EmailField(verbose_name='邮箱')
    password = models.CharField(max_length='50', verbose_name='密码')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '用户'

    def __str__(self):
        return self.username
    