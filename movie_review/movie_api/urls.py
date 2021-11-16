from django.urls import path
from .import views

urlpatterns = [
    path('', views.ApiOverview, name='ApiOverview'),
    path('movie-list/', views.MoviesList, name='ShowMovies'),
    path('users-list/', views.UsersList, name='ShowUsers'),
    path('user-create/', views.CreateUser, name='CreateUser'),
    path('category/', views.Category1, name='Category'),
    path('review/', views.Review1, name='Review'),
    path('review-list/', views.ReviewShow, name='ReviewList'),
    path('rating-insert/', views.Rating1, name='Rating-Insert'),
    path('rating/', views.Ratingshow, name='Rating'),

]
