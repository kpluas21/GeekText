from django.urls import path
from . import views
from django.conf import settings

#By default, shows a list of all the books in the db
urlpatterns = [
    path('', views.getBook),
    path('get/', views.getBook),
    path('post/', views.postBook),
    path('bestsellers/', views.postTopSellers),
    path('searchbygenre/<str:genreSearch>', views.postBookByGenre),
    path('updatepricing/<str:publisher>/<int:percent>/', views.UpdatePriceByPublisher.as_view()),
    path('resetpricing/', views.ResetPricing.as_view()),
    path('searchbyrating/<int:ratingSearch>/',views.sortByRating),
    # path('addbook/', views.addbook, name='addbook')

]