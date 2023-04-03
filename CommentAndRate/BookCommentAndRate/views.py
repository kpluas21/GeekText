from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Book, BookRating, BookComment
from .serializers import BookRatingSerializer, BookCommentSerializer
from rest_framework.decorators import api_view
from .models import BookComment
from .forms import CommentForm
from datetime import datetime
from django.contrib.auth.models import User
from .models import BookRating
from .forms import RatingForm
from datetime import datetime

@api_view(['POST'])
def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_text = form.cleaned_data['comment_text']
            user_id = form.cleaned_data['user_id']
            book_id = form.cleaned_data['book_id']
            user = User.objects.get(pk=user_id)
            book = Book.objects.get(pk=book_id)
            comment = BookComment(comment_text=comment_text, user=user, book=book, timestamp=datetime.now())
            comment.save()
            return HttpResponse(status=204)
    else:
        form = CommentForm()
    return render(request, 'comment.html', {'form': form})

@api_view(['POST'])
def add_rating(request):
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            value = form.cleaned_data['value']
            user_id = form.cleaned_data['user_id']
            book_id = form.cleaned_data['book_id']
            user = User.objects.get(pk=user_id)
            book = Book.objects.get(pk=book_id)
            rating = BookRating(value=value, user=user, book=book, timestamp=datetime.now())
        if rating < 1 or rating > 5:
            return Response({'error': 'Rating must be between 1 and 5'})
        else:
            book.rating = rating
            book.save()
            rating.save()
            return Response({'message': 'Rating updated successfully'})
    else:
        return Response({'error': 'Rating field is required'})
