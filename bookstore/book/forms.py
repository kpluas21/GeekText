from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class createBookForm(ModelForm):
    class Meta:
        model=Book
        fields='__all__'
