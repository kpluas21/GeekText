from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, null = True, on_delete=models.CASCADE)
    username = models.CharField(max_length = 200, default= '')
    password = models.CharField(max_length=200, null = True)
    address = models.CharField(default = '', max_length=100)
    name = models.CharField(max_length=200, null = True)
    email = models.EmailField(default = '', max_length= 200)
    


    def __str__(self):
        return str(self.username)
    
class CreditCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default = '')
    card_num = models.BigIntegerField()
    card_name = models.CharField(max_length = 200)
    cvc = models.IntegerField()
    








