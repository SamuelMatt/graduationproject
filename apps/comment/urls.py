from django.conf.urls import url

from . import views

app_name = 'comment'
urlpatterns = [
    url(r'^comment/post/(?P<post_id>[0-9]+)/$', views.comment, name='comment'),
]