from rest_framework import serializers

from .models import Users, Category, Movie, Review, Rating
from django.contrib.auth.hashers import make_password


class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class ApiSerializer5(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'NAME', 'EMAIL', 'CONTACT')


class ApiSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'NAME', 'EMAIL', 'CONTACT', 'PASSWORD')

    def create(self, validated_data):
        user = Users.objects.create(
            EMAIL=validated_data['EMAIL'],
            NAME=validated_data['NAME'],
            CONTACT=validated_data['CONTACT'],
            PASSWORD=make_password(validated_data['PASSWORD'])
        )
        return user


class ApiSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ApiSerializer3(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'Review', 'MID_id', 'UID_id', 'LIKES', 'DISLIKES')


class ApiSerializer4(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('Count', 'MID_id', 'UID_id')
