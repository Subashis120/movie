from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import ApiSerializer
from .models import Movie, Users, Rating, Review, Category
from django.contrib.auth.hashers import make_password

# Create your views here.


@api_view(['Get'])
def ApiOverview(request):
    api_urls = {
        'List': '/movie-list/',
        'U-List': '/users-list/',
        'Detail View': '/movie-detail/<int:id>',
        'UCreate': '/user-create/',
        'MCreate': '/movie-create/',
        'U-update': '/user-update/<int:id>',
        'M-update': '/movie-update/<int:id>',
        'U-Delete': '/user-delete/',
        'M-Delete': '/movie-delete/',
        'C-List': '/category/',
        'R-List': '/review/',
        'Rat-List': '/rating/',

    }
    return Response(api_urls)


@api_view(['Get'])
def MoviesList(request):
    movies = Movie.objects.all()
    serializer = ApiSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['Get'])
def UsersList(request):
    users = Users.objects.all()
    serializer = ApiSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['Post'])
def CreateUser(request):
    serializer4 = ApiSerializer(data=request.data)
    if serializer4.is_valid():
        serializer4.save()

    return Response(serializer4.data)


@api_view(['Post'])
def Rating(request):
    serializer1 = ApiSerializer(data=request.data)

    if serializer1.is_valid():
        serializer1.save()

    return Response(serializer1.data)


@api_view(['Post'])
def Review(request):
    serializer2 = ApiSerializer(data=request.data)

    if serializer2.is_valid():
        serializer2.save()

    return Response(serializer2.data)


@api_view(['Get'])
def Category(request):
    category = Category.objects.all()
    serializer3 = ApiSerializer(category, many=True)
    return Response(serializer3.data)

