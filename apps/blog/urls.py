from django.conf.urls import url

from . import views

app_name = 'blog'

urlpatterns = [
    url('', views.index, name='index'),
    url(r'^post/(?P<id>[0-9]+)/$', views.detail, name='detail'),
]
