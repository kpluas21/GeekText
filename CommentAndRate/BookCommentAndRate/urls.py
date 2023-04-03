from django.urls import path
from . import views
from django.conf import settings
from .views import add_comment
from .views import add_rating

urlpatterns = [

path('comment/', add_comment, name='create_comment'),
path('rating/', add_rating, name='create_rating'),

] 
