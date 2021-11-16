from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import ApiSerializer, ApiSerializer1, ApiSerializer2, ApiSerializer3, ApiSerializer4, ApiSerializer5
from .models import Movie, Users, Rating, Review, Category


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
        'Rat-insert': '/rating-insert/',
        'Rat-List': '/rating/',
        'Review-show': '/review-list/',

    }
    return Response(api_urls)


@api_view(['GET'])
def MoviesList(request):
    movies = Movie.objects.all()
    serializer = ApiSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def UsersList(request):
    users = Users.objects.all()
    serializer = ApiSerializer5(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def Ratingshow(request):
    rating = Rating.objects.all()
    serializer1 = ApiSerializer4(rating, many=True)
    return Response(serializer1.data)


@api_view(['GET'])
def Category1(request):
    cat = Category.objects.all()
    serializer3 = ApiSerializer2(cat, many=True)
    return Response(serializer3.data)


@api_view(['GET'])
def ReviewShow(request):
    review = Review.objects.all()
    serializer2 = ApiSerializer3(review, many=True)
    return Response(serializer2.data)


@api_view(['Post'])
def CreateUser(request):
    serializer4 = ApiSerializer1(data=request.data)
    if serializer4.is_valid():
        serializer4.save()
    return Response(serializer4.data)


@api_view(['Post'])
def Review1(request):
    serializer2 = ApiSerializer3(data=request.data)
    if serializer2.is_valid():
        serializer2.save()
    return Response(serializer2.data)


@api_view(['Post'])
def Rating1(request):
    serializer1 = ApiSerializer4(data=request.data)
    if serializer1.is_valid():
        serializer1.save()
    return Response(serializer1.data)




