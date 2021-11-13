from django.contrib import admin
from .models import Users, Category, Movie, Review, Rating


# Register your models here.
admin.site.register(Users)
admin.site.register(Category)
admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(Rating)

