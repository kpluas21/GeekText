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
    title  = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    year   = models.PositiveSmallIntegerField()
    genre  = models.CharField(max_length=200)
    isbn   = models.IntegerField()
    copiesSold=models.PositiveSmallIntegerField()
    

    def __str__(self):
        return str(self.title)

class Customer(models.Model):
    userName = models.OneToOneField(User, null = True, on_delete=models.CASCADE)
    email    = models.EmailField(null = True)
    homeAddr = models.CharField(max_length = 200, null=True)
    name     = models.CharField(max_length = 200, null=True)

    def __str__(self):
        return str(self.userName)


