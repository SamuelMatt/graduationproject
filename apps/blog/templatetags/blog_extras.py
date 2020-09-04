from django import template

from ..models import Post, Category, Tag

register = template.Library()


@register.inclusion_tag('blog/inclusions/_recent_post.html', takes_context=True)
def show_recent_post(context, num=5):
    return {
        'recent_post_list': Post.objects.all().order_by('-created_time')[:num],
    }


@register.inclusion_tag('blog/inclusions/_archive.html', takes_context=True)
def show_archive(context):
    return {
        'date_list': Post.objects.dates('created_time', 'month', order='DESC'),
    }


@register.inclusion_tag('blog/inclusions/_categorie.html', takes_context=True)
def show_categorie(context):
    return {
        'category_list': Category.objects.all(),
    }


@register.inclusion_tag('blog/inclusions/_tag.html', takes_context=True)
def show_tag(context):
    return {
        'tag_list': Tag.objects.all(),
    }
