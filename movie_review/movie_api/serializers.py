from rest_framework import serializers

from .models import Users, Category, Movie, Review, Rating


class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'NAME', 'EMAIL', 'CONTACT', 'PASSWORD')


class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'
