from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=('title', 'author', 'year', 'isbn', 'genre', 'copiesSold')

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=('title', 'author', 'genre')

class PublisherPatchingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=('price',)
    