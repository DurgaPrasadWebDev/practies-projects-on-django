from django.db import models
import uuid


class Actor(models.Model):
    GENDER = {
        ('M', 'Male'),
        ('F', 'FeMale')
    }
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER)
    date_of_birth = models.DateField()
    unique_id = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return 'Actor name is {} and unique id is {}'.format(self.name, self.unique_id)


class Movie(models.Model):
    title = models.CharField(max_length=400)
    date_of_release = models.DateField()
    actors = models.ManyToManyField(Actor, through='MovieCast', through_fields=('movie', 'cast'))

    def __str__(self):
        return 'The Movie title is {}'.format(self.title)


class MovieCast(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_casts',
                              related_query_name='movie_cast')
    cast = models.ForeignKey(Actor, on_delete=models.CASCADE, related_query_name='movie_cast',
                             related_name='movie_casts')
    role = models.CharField(max_length=50)
    remuneration_in_usd = models.FloatField(default=0)

    def __str__(self):
        return 'The Movie is {} and Actor is {} and Role is {} and Remuneration'.format(self.movie,
                                                                                        self.cast, self.role,
                                                                                        self.remuneration_in_usd)


class MovieRating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_ratings',
                              related_query_name='movie_rating')
    rating = models.IntegerField()
    no_of_ratings = models.IntegerField()

    def __str__(self):
        return 'The Movie is {} and Rating is {} and no_of_rating is {}'.format(self.movie, self.rating,
                                                                                self.no_of_ratings)
