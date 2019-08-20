from django.db import models


class Actor(models.Model):
    name = models.CharField(max_length=50)
    GENDER_LIST = [('F','Female'),('M','Male')]
    gender = models.CharField(max_length=1,choices=GENDER_LIST,blank=True)
    birth_date = models.DateField()


class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    actors = models.ManyToManyField(Actor)


class MovieCast(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    cast = models.ForeignKey(Actor,on_delete=models.CASCADE)
    role = models.CharField(max_length=60)


class MovieRating(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    rating = models.IntegerField()
    no_of_ratings = models.IntegerField()