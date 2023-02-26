from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Book
from .forms import *
from .serializer import BookSerializer, GenreSerializer
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
