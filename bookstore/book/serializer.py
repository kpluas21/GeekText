from rest_framework import serializers
from .models import Book

#Our main serializer that simply grabs all the books and shows off each of their fields
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=('title', 'author', 'year', 'isbn', 'genre', 'copiesSold', 'price', 'publisher', 'rating')

#Used just to list books by their genres
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=('title', 'author', 'genre')

#Used to pull up books based on their publishers with the purpose of editing the prices
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
    
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields=('title', 'author', 'rating', 'price')