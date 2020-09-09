from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.utils.text import slugify

from pure_pagination.mixins import PaginationMixin
import markdown
from markdown.extensions.toc import TocExtension

from .models import Category, Tag, Post

# Create your views here.


class IndexView(PaginationMixin, ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    paginate_by = 10


class SearchView(IndexView):
    def get_context_data(self):
        context = super().get_context_data()
        context.update({
            'q': self.request.GET.get('q', '')
        })
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if not q:
            return queryset
        return queryset.filter(Q(title__icontains=q) | Q(body__icontains=q))


class ArchiveView(IndexView):
    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        return (
            super().get_queryset().filter(created_time__year=year, created_time__month=month)
        )


class CategoryView(IndexView):
    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super().get_queryset().filter(category=cate)


class TagView(IndexView):
    def get_queryset(self):
        t = get_object_or_404(Tag, pk=self.kwargs.get("pk"))
        return super().get_queryset().filter(tags=t)


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        self.object.increase_view()
        return response

