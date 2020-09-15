from django.contrib import admin

from .models import User

# Register your models here.


@admin.register(User)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['username', 'nikename']
    fields = ['username', 'nikename', 'email']
