from django.contrib import admin
from .models import Book, BookComment
from . import models
admin.site.register(Book)
# admin.site.register(Customer)

# Register your models here.
admin.site.register(models.BookRating)
admin.site.register(models.BookComment)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('Username', 'Comment',)
    date_hierarchy = 'created'
