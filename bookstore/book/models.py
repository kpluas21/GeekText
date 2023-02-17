from django.db import models
from django.contrib.auth.models import User

#here we define default values for blank fields
def default_author():
    return {"author": "Unknown Author"}

def default_genre():
    return {"genre" : "Unknown Genre"}

def default_title():
    return {"title" : "Unknown Title"}


class Book(models.Model):
    title  = models.CharField(max_length=200, default=default_title(), blank=False)
    author = models.CharField(max_length=200, default=default_author(), blank=False)
    year   = models.PositiveSmallIntegerField(null=True)
    genre  = models.CharField(max_length=200, default=default_genre, blank=False)
    isbn   = models.CharField(max_length=13, unique=True, blank=False)
    copiesSold=models.PositiveSmallIntegerField(null=True, default="0")
    

    def __str__(self):
        return str(self.title)

class Customer(models.Model):
    userName = models.OneToOneField(User, null = True, on_delete=models.CASCADE)
    email    = models.EmailField(null = True)
    homeAddr = models.CharField(max_length = 200, null=True)
    name     = models.CharField(max_length = 200, null=True)

    def __str__(self):
        return str(self.userName)


