from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.BookRating)
admin.site.register(models.BookComment)
