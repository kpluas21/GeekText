from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, status
from .models import Book
from .forms import *
from .serializer import BookSerializer, GenreSerializer, PublisherPatchingSerializer, PriceResetSerializer
from django.http import HttpResponse


@api_view(['GET'])
def getBook(request):
    book = Book.objects.all()
    serializer = BookSerializer(book, many=True)
    return Response(serializer.data)

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
# @api_view(['GET'])
# def sortByRating(request)
    
# def addbook(request):
#     form=createBookForm()
#     if request.method=='POST':
#         form=createBookForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect('/')
    
#     context={'form':form}
#     return render(request, 'book/addbook.html',context)

# Create your views here.
