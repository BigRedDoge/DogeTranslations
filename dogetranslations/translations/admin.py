from django.contrib import admin
from .models import Post, Series, Book

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'book_id', 'post_slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'post_slug': ('title',)}

class SeriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'series_slug', 'created_on')
    list_filter = ("title",)
    search_fields = ['title']
    prepopulated_fields = {'series_slug': ('title',)}

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'series', 'book_slug', 'created_on')
    list_filter = ("title",)
    search_fields = ['title']
    prepopulated_fields = {'book_slug': ('title',)}

admin.site.register(Post, PostAdmin)
admin.site.register(Series, SeriesAdmin)
admin.site.register(Book, BookAdmin)