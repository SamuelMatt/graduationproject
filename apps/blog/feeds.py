from django.contrib.syndication.views import Feed

from .models import Post


class AllPostsRssFeed(Feed):
    title = 'blogproject'

    link = '/'

    description = 'blogproject 全部文章'

    def items(self):
        return Post.objects.all()

    def item_title(self, item):
        return f'[{item.category}] {item.title}'

    def item_description(self, item):
        return item.body_html
