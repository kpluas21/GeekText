from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    #user = models.OneToOneField(User, null = True, on_delete=models.CASCADE)
    username = models.CharField(max_length = 200, default= '', primary_key=True)
    password = models.CharField(null = True, max_length=200)
    address = models.CharField(default = '', max_length=100)
    name = models.CharField(max_length=200, null = True)
    email = models.EmailField(default = '', max_length= 200)
    

    def __str__(self):
        return str(self.username)
    


class CreditCard(models.Model):
    username = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name= 'user', db_constraint=False)
    card_num = models.BigIntegerField()
    card_name = models.CharField(max_length = 200)
    cvv = models.IntegerField()

    def __str__(self):
        return str(self.username)


#3/14 could not migrate the new fields because of duplicates in the database, have to clean the database
    
    








