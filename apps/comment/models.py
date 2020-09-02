from django.db import models

from apps.blog.models import Post

# Create your models here.


class Comment(models.Model):
    name = models.CharField(max_length=50, verbose_name='名字')
    email = models.EmailField(verbose_name='邮箱')
    url = models.URLField(blank=True, verbose_name='网址')
    text = models.TextField(verbose_name='内容')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    post = models.ForeignKey(Post, verbose_name='文章', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name
        # ordering = ['-created_time']

    def __str__(self):
        return f'{self.name}: {self.text[:20]}'
