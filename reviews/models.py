from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings

#Modelo para categoria
class Category(models.Model):

    name = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    createdAt = models.DateField(blank=True, null=True)
    updatedAt = models.DateField(blank=True, null=True)

    def __str__(self):

        return self.name

#Modelo para pelicula

class Movie(models.Model):

    poster = models.TextField()
    movieName = models.CharField(max_length=25)
    description = models.CharField(max_length=255)
    createdAt = models.DateField(blank=True, null=True)
    updatedAt = models.DateField(blank=True, null=True)

    category = models.ForeignKey(

        Category, related_name="categorys", on_delete=models.CASCADE
    )

    def __str__(self):

        return self.movieName


#Modelo para la rese;a
class Review(models.Model):
    
    comment = models.TextField()
    ranking = models.IntegerField()
    createdAt = models.DateField(blank=True, null=True)
    updatedAt = models.DateField(blank=True, null=True)

    movie = models.ForeignKey(

        Movie, related_name="movies", on_delete=models.CASCADE
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)    

    def __str__(self):

        return self.comment
