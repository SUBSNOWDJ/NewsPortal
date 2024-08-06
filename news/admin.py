from django.contrib import admin
from .models import Author, Category, Post, PostCategory, Comment


class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Post._meta.get_fields()]
    list_filter = ('Category', 'Author')
    search_fields = ('title', 'creation_time')

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Comment)

# Register your models here.