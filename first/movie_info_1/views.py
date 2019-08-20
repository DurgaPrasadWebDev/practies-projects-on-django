from .models import *
from django.db import connection
from django.db.models import *
from datetime import datetime,date

def date_convert_to_string(date):
    return date.strftime("%d-%b-%Y")


def movie_convert_to_dictionary(movie):
    movie_details = dict()
    movie_details['title'] = movie['movie__title']
    movie_details['date_of_release'] = date_convert_to_string(movie['movie__date_of_release'])
    try:
        movie_details['max_no_of_actors'] = movie['max_nof_actors']
    except KeyError:
        pass
    return movie_details


def get_movies_with_no_of_actors():
    movie_casts = MovieCast.objects.values('movie__title','movie__date_of_release','cast').distinct()
    movie_with_max_no_actors = movie_casts.values('movie__title','movie__date_of_release').annotate(max_nof_actors=Count('movie__title')).order_by('movie__title')
    movies_with_max_no_actor_list = [movie_convert_to_dictionary(each_movie) for each_movie in movie_with_max_no_actors]
    return movies_with_max_no_actor_list

def get_average_min_and_max_remuneration_of_movie(movie):
    movie_cast = MovieCast.objects.filter(movie__title=movie)
    movie_with_max_and_min_and_avg_remuneration = movie_cast.values('movie__title').aggregation(max_remuneration=Max('remuneration_in_usd'),min_remuneration=Min('remuneration_in_usd'),avg_remuneration=Avg('remuneration_in_usd'))
    return movie_with_max_and_min_and_avg_remuneration

def get_movies_with_min_age_of_actor():
    movie_cast = MovieCast.objects.annotate(age=ExpressionWrapper(datetime.now().date()-F('cast__date_of_birth'),output_field=DurationField()))
    movies_with_min_age = movie_cast.values('movie__title','movie__date_of_release').annotate(min_age=Min('age'))
    return movies_with_min_age

def get_movies_with_out_role7():
    movies = Movie.objects.filter(~Q(movie_cast__role='role7'))
    movies_with_out_role7 = movies.values('title','date_of_release')
    return movies_with_out_role7
def get_movies_more_than_10_female():
    unique_movie_cast = MovieCast.objects.values('movie__title','movie__date_of_release','cast__name','cast__gender').distinct()
    movies = unique_movie_cast.filter(cast__gender='F').values('movie__title','movie__date_of_release').annotate(no_of_female_actors=Count('movie__title'))
    movies_more_than_10_female = movies.filter(no_of_female_actors__gt=10)
    return movies_more_than_10_female

def get_movies_deference_between_no_of_male_and_female_actors():
    no_male_actors = Actor.objects.filter(movie=OuterRef('pk')).distinct().filter(gender='M').aggregate(no_of_male=Count('gender'))
    no_female_actors = Actor(movie=OuterRef('pk')).distinct().filter(gender='F').count()
    movies_with_no_of_male_and_female_actors = Movie.objects.annotate(no_of_male=Subquery(no_male_actors),no_of_female=Subquery(no_female_actors))
    return movies_with_no_of_male_and_female_actors
