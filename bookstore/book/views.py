from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from .models import Book
from .forms import *
from .serializer import BookSerializer, GenreSerializer, PublisherPatchingSerializer
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

@api_view(['PATCH'])
def updateBookPricesByPublisher(request, publisherSearch, percent):
    book = Book.objects.filter(publisher = publisherSearch)
    serializer = PublisherPatchingSerializer(book, data=request.data ,partial=True)
    return Response(serializer.data)

class UpdatePriceByPublisher(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = PublisherPatchingSerializer
    lookup_field = 'publisher'
    
    def partial_update(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(publisher=kwargs['publisher'])
        price = kwargs['price']
        queryset.update(price=price)
        return Response(status=status.HTTP_200_OK)

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
