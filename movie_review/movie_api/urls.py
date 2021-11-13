from django.urls import path
from .import views

urlpatterns = [
    path('', views.ApiOverview, name='ApiOverview'),
    path('movie-list/', views.MoviesList, name='ShowMovies'),
    path('users-list/', views.UsersList, name='ShowUsers'),
    path('user-create/', views.CreateUser, name='CreateUser'),
    path('category/', views.Category, name='Category'),
    path('review/', views.Review, name='Review'),
    path('rating/', views.Rating, name='Review'),

]
