from django.db import models
from django.contrib.auth.models import User

import book

#here we define default values for blank fields
def default_author():
    return {"author": "Unknown Author"}

def default_genre():
    return {"genre" : "Unknown Genre"}

def default_title():
    return {"title" : "Unknown Title"}


class Book(models.Model):
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    title  = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    year   = models.PositiveSmallIntegerField()
    genre  = models.CharField(max_length=200)
    isbn   = models.IntegerField()
    copiesSold=models.PositiveSmallIntegerField()
    price  = models.IntegerField()
    publisher = models.CharField(max_length=200, null=True)
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    #with book rating and commenting
    

    def __str__(self):
        return str(self.title)

#The customer class however someone else might be doing this one?
# class Customer(models.Model):
#     userName = models.OneToOneField(User, null = True, on_delete=models.CASCADE)
#     email    = models.EmailField(null = True)
#     homeAddr = models.CharField(max_length = 200, null=True)
#     name     = models.CharField(max_length = 200, null=True)

#     def __str__(self):
#         return str(self.userName)


class BookRating(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=((1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')))
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.book.title} ({self.rating}) by {self.user.username} on {self.timestamp}'

class BookComment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.book.title} ({self.comment}) by {self.user.username} on {self.timestamp}'


