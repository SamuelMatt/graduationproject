from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify
import re
import markdown
from markdown.extensions.toc import TocExtension

from .models import Category, Tag, Post

# Create your views here.


def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def detail(request, id):
    post = get_object_or_404(Post, id=id)
    md = markdown.Markdown(extensions=(
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        TocExtension(slugify=slugify),
    ))
    post.body = md.convert(post.body)

    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    post.toc = m.group(1) if m is not None else ''

    return render(request, 'blog/detail.html', context={'post': post})


def category(request, id):
    cate = get_object_or_404(Category, id=id)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def tag(request, id):
    t = get_object_or_404(Tag, id=id)
    post_list = Post.objects.filter(tags=t).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def archive(request, year, month):
    post_list = Post.objects.filter(
        created_time__year=year,
        created_time__month=month,
        ).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})
