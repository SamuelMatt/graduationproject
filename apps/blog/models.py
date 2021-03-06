from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.utils.html import strip_tags
from django.utils.text import slugify
from django.utils.functional import cached_property

import markdown
from markdown.extensions.toc import TocExtension

# Create your models here.


def generate_rich_content(value):
    md = markdown.Markdown(
        extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            TocExtension(slugify=slugify),
        ]
    )
    content = md.convert(value)
    toc = md.toc
    return {'content': content, 'toc': toc}


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='分类名')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    
    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name='标签名')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    body = models.TextField(verbose_name='正文')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    excerpt = models.CharField(max_length=200, blank=True, verbose_name='摘要')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='分类')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='标签')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    view = models.PositiveIntegerField(default=0, editable=False, verbose_name='阅读')

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        ordering = ["-created_time"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        md = markdown.Markdown(extensions=(
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ))

        self.excerpt = strip_tags(md.convert(self.body))[:54]
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def increase_view(self):
        self.view += 1
        self.save(update_fields=['view'])

    @property
    def toc(self):
        return self.rich_content.get('toc', '')

    @property
    def body_html(self):
        return self.rich_content.get('content', '')

    @cached_property
    def rich_content(self):
        return generate_rich_content(self.body)
