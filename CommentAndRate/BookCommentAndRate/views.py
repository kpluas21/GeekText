from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, status
from .models import Book
from .forms import *
from .serializer import BookSerializer, GenreSerializer, PublisherPatchingSerializer, PriceResetSerializer, RatingSerializer, BookRatingSerializer, BookCommentSerializer
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Book, BookRating, BookComment
from rest_framework.decorators import api_view
from .models import BookComment
from .forms import CommentForm
from datetime import datetime
from django.contrib.auth.models import User
from .models import BookRating
from .forms import RatingForm
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

#Default view, shows all the books in the DB and their fields
@api_view(['GET'])
def getBook(request):
    book = Book.objects.all()
    serializer = BookSerializer(book, many=True)
    return Response(serializer.data)

#Post method for adding books to the DB
@api_view(['POST'])
def postBook(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#Lists the top 10 books that have the most copies sold
@api_view(['GET'])
def postTopSellers(request):
    book = Book.objects.order_by('-copiesSold')[:10]
    serializer = BookSerializer(book , many=True)
    return Response(serializer.data)

#Given a genre, display all the books of that genre
@api_view(['GET'])
def postBookByGenre(request, genreSearch):
    book = Book.objects.filter(genre=genreSearch)
    serializer = GenreSerializer(book, many=True)
    return Response(serializer.data)

class UpdatePriceByPublisher(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = PublisherPatchingSerializer
    lookup_field = 'publisher'
    
    def partial_update(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(publisher=kwargs['publisher'])
        percent = kwargs['percent']
        for book in queryset:
            book.price *= (1 - percent / 100)
            book.save()
        return Response(status=status.HTTP_200_OK)

#For testing purposes, resets price for all books to 50
class ResetPricing(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = PriceResetSerializer
    
    def partial_update(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        for book in queryset:
            book.price = 50
            book.save()
        return Response(status=status.HTTP_200_OK)

#Given a rating, return the books equal to or greater than said rating
@api_view(['GET'])
def sortByRating(request, ratingSearch):
    book = Book.objects.filter(rating__gte=ratingSearch)
    serializer = RatingSerializer(book, many=True)
    return Response(serializer.data)


# Create your views here.
@csrf_exempt
@api_view(['POST'])
def add_comment(request):
    comment = None
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
    if comment is None:
        comment = BookComment()
    return render(request, 'comment.html', {'form': form, 'comment': comment})

@csrf_exempt
@api_view(['POST'])
def add_rating(request):
    if request.method == 'POST':
        form = RatingForm(request.POST)
        rating = None
        if form.is_valid():
            value = form.cleaned_data['value']
            user_id = form.cleaned_data['user_id']
            book_id = form.cleaned_data['book_id']
            user = User.objects.get(pk=user_id)
            book = Book.objects.get(pk=book_id)
            rating = BookRating(value=value, user=user, book=book, timestamp=datetime.now())
            if rating.value < 1 or rating.value > 5:
                return Response({'error': 'Rating must be between 1 and 5'})
            else:
                book.rating = rating
                book.save()
                rating.save()
                return Response({'message': 'Rating updated successfully'})
        else:
            return Response({'error': 'Rating field is required'})



@api_view(['GET'])
def list_comments(request, book_id):
    comments = BookComment.objects.filter(book=book_id)
    serializer =BookCommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_average_rating(request, book_id):
    ratings = BookRating.objects.filter(book=book_id)
    if len(ratings) > 0:
        total = sum([rating.rating for rating in ratings])
        average = total / len(ratings)
        return Response({'average_rating': average})
    return Response({'average_rating': 0})
