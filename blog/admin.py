from django.contrib import admin
from blog.models import Post, Comment

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'thumbnail'] #admin 페이지에서 보여줄 필드

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass