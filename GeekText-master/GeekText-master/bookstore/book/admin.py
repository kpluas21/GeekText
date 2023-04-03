from django.contrib import admin
from .models import Book, Author #, Customer

admin.site.register(Book)
admin.site.register(Author)
# admin.site.register(Customer)

# Register your models here.
