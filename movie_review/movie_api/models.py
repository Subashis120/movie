from django.db import models

# Create your models here.


class Users(models.Model):
    NAME = models.CharField(max_length=30, null=False, blank=False)
    EMAIL = models.EmailField(max_length=255, null=False, blank=False, unique=True)
    CONTACT = models.CharField(max_length=10, null=False, blank=False)
    PASSWORD = models.CharField(max_length=60, null=False, blank=False)

    def __str__(self):
        return self.NAME


class Category(models.Model):
    NAME = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.NAME


class Movie(models.Model):
    NAME = models.TextField(blank=False)
    COVER = models.ImageField(upload_to="cover_pic", blank=True)
    CatID_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    CAST = models.TextField(blank=False)
    DESCRIPTION = models.TextField(blank=False)

    def __str__(self):
        return self.NAME


class Review(models.Model):
    Review = models.TextField()
    MID_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    UID_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    LIKES = models.IntegerField()
    DISLIKES = models.IntegerField()

    def __str__(self):
        return self.Review


class Rating(models.Model):
    Count = models.IntegerField()
    MID_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    UID_id = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.Count)
