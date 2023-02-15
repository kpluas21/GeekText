from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title  = models.CharField(max_length=200,null=True)
    author = models.CharField(max_length=200,null=True)
    year   = models.PositiveSmallIntegerField(null=True)
    isbn   = models.CharField(max_length=13, unique=True)
    
    def __str__(self):
        return str(self.title)

class Customer(models.Model):
    userName = models.OneToOneField(User, null = True, on_delete=models.CASCADE)
    email    = models.EmailField(null = True)
    homeAddr = models.CharField(max_length = 200, null=True)
    name     = models.CharField(max_length = 200, null=True)

    def __str__(self):
        return str(self.userName)


