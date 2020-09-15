from django.db import models
from django.contrib.auth.models import User

from apps.blog.models import Post

# Create your models here.


class Comment(models.Model):
    text = models.TextField(verbose_name='内容')
    author = models.ForeignKey(User, verbose_name='作者')
    post = models.ForeignKey(Post, verbose_name='文章', on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name
        ordering = ['-created_time']

    def __str__(self):
        return f'{self.author}: {self.text[:20]}'
