from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=('title', 'author', 'year', 'isbn', 'genre', 'copiesSold', 'price', 'publisher',)

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=('title', 'author', 'genre')

class PublisherPatchingSerializer(serializers.ModelSerializer):
    price = serializers.IntegerField(read_only=False)

    class Meta:
        model=Book
        fields=('title', 'author', 'publisher', 'price',)

class PriceResetSerializer(serializers.ModelSerializer):
    price = serializers.IntegerField(read_only=False)

    class Meta:
        model=Book
        fields=('price',)
    