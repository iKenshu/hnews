from django.contrib import admin

# Register your models here.
from .models import New, Comment

@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('new', 'author', 'text')