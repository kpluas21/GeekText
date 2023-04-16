from django.urls import path
from . import views
from django.conf import settings
from .views import add_comment, add_rating, list_comments, get_average_rating


#By default, shows a list of all the books in the db
urlpatterns = [

path('', views.getBook),
path('bookcomment/', add_comment, name='create_comment'),
path('bookrating/', add_rating, name='create_rating'),
path('comments/<int:book_id>/', list_comments, name='list_comments')

]
