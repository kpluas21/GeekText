from rest_framework import serializers
from .models import Book, BookRating, BookComment

class BookRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookRating
        fields = '__all__'

class BookCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookComment
        fields = '__all__'
