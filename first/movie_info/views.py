from .models import *
from django.db.models import *
from django.db import connection


def date_convert_to_string(date):
    return date.strftime("%d-%b-%Y")


def actor_convert_dictionary(actor):
    actor_details = dict()
    actor_details['actor_id'] = actor.id
    actor_details['name'] = actor.name
    actor_details['date_of_birth'] = date_convert_to_string(actor.date_of_birth)
    actor_details['unique_id'] = str(actor.unique_id)
    return actor_details


def movie_convert_to_dictionary(movie):
    movie_details = dict()
    movie_details['title'] = movie['movie__title']
    movie_details['date_of_release'] = date_convert_to_string(movie['movie__date_of_release'])

    return movie_details


def get_movie_titles_starts_with_given_word(match_word):
    movie_title_list = Movie.objects.filter(title__istartswith=match_word).values('title')
    return movie_title_list


def get_movie_titles_ends_with_given_word(match_word):
    movie_title_list = Movie.objects.filter(title__iendswith=match_word).values('title')
    return movie_title_list


def get_movie_titles_contains_with_given_word(match_word):
    movie_title_list = Movie.objects.filter(title__icontains=match_word).values('title')
    return movie_title_list


def get_top_paid_actor():
    top_paid_actor = MovieCast.objects.order_by('-remuneration_in_usd', 'cast__name').values('cast__id', 'cast__name',
                                                                                             'cast__gender',
                                                                                             'cast__date_of_birth',
                                                                                             'cast__unique_id')[:1]
    return top_paid_actor


def get_least_paid_actor():
    least_paid_actor = MovieCast.objects.order_by('remuneration_in_usd', 'cast__name').values('cast__id', 'cast__name',
                                                                                              'cast__gender',
                                                                                              'cast__date_of_birth',
                                                                                              'cast__unique_id')[:1]
    return least_paid_actor


def get_actor_details_born_in_given_month(month):
    actors = Actor.objects.filter(date_of_birth__month=month).order_by('-date_of_birth')

    actors_list = []
    for each_actor in actors:
        actor_details = actor_convert_dictionary(each_actor)
        actors_list.append(actor_details)
    return actors_list


def get_actor_movie_list_given_by_uuid(unique_id):
    movies_list = MovieCast.objects.filter(cast__unique_id=unique_id).values('movie_id', 'movie__title',
                                                                             'movie__date_of_release').order_by(
        '-movie__date_of_release').distinct()

    movie_details_list = []
    for each_movie in movies_list:
        movie_details = movie_convert_to_dictionary(each_movie)
        movie_details_list.append(movie_details)
    return movie_details_list


def get_actors_details_with_remuneration_between_50000_and_150000():
    actors_details_list = MovieCast.objects.filter(remuneration_in_usd__gt=50000,
                                                   remuneration_in_usd__lt=150000).prefetch_related('cast').order_by(
        'cast__name')

    actors_list = []
    for each_actor in actors_details_list:
        actor_details = actor_convert_dictionary(each_actor.cast)
        if actor_details not in actors_list:
            actors_list.append(actor_details)
    return actors_list


def get_movies_more_than_20000_of_5_star_rating():
    movie_list = Movie.objects.filter(movie_rating__rating=5, movie_rating__no_of_ratings__gt=20000).values('title',
                                                                                                            'date_of_release')
    return movie_list


def get_actors_acted_in_titanic_or_avatar_or_avenger_end_game():
    movie_casts = MovieCast.objects.filter(movie__title__in=['Titanic', 'Avatar', 'Avengers Endgame']).prefetch_related(
        'cast').order_by('-remuneration_in_usd')

    actor_details_list = []
    for each_movie_cast in movie_casts:
        actor_details = actor_convert_dictionary(each_movie_cast.cast)
        if actor_details not in actor_details_list:
            actor_details_list.append(actor_details)
    return actor_details_list


def get_actors_acted_in_titanic_or_avatar_and_not_acted_in_inception_and_clash_of_the_titan():
    movie_casts = MovieCast.objects.filter((~Q(movie__title='Inception') & ~Q(movie__title='Clash of the Titans')) & (
                Q(movie__title='Titanic') | Q(movie__title='Avatar'))).order_by('-remuneration_in_usd')

    actor_details_list = []
    for each_movie_cast in movie_casts:
        actor_details = actor_convert_dictionary(each_movie_cast.cast)
        if actor_details not in actor_details_list:
            actor_details_list.append(actor_details)
    return actor_details_list


def get_complete_movie_details(movie_title):
    movie_casts = MovieCast.objects.filter(movie__title=movie_title).prefetch_related('cast', 'movie')
    movie_ratings = MovieRating.objects.filter(movie__title=movie_title)
    movie_complete_details = dict()
    movie = {
        "movie_title": movie_casts[0].movie.title,
        "date_of_release": date_convert_to_string(movie_casts[0].movie.date_of_release)
    }
    cast = [
        {
            "actor": actor_convert_dictionary(each_movie_cast.cast),
            "role": each_movie_cast.role,
            "remuneration_in_usd": each_movie_cast.remuneration_in_usd
        } for each_movie_cast in movie_casts
    ]
    movie_rating_list = []
    for each_movie_rating in movie_ratings:
        s = {
            "no_of_ratings": each_movie_rating.no_of_ratings,
            "rating": each_movie_rating.rating
        }
        movie_rating_list.append(s)
    movie_complete_details["movie"] = movie
    movie_complete_details["cast"] = cast
    movie_complete_details["ratings"] = movie_rating_list
    return movie_complete_details

