from datetime import date
from .models import *
import uuid

ACTOR = [
    {
        "name": 'actor1',
        "gender": 'M',
        "date_of_birth": date(1990, 12, 3),
        "born_in_country": "country1",
    },
    {
        "name": 'actor2',
        "gender": 'F',
        "date_of_birth": date(1994, 9, 4),
        "born_in_country": "country2",
    },
    {
        "name": 'actor3',
        "gender": 'M',
        "date_of_birth": date(1994, 3, 4),
        "born_in_country": "country3",
    },
    {
        "name": 'actor4',
        "gender": 'F',
        "date_of_birth": date(1996, 11, 1),
        "born_in_country": "country1",
    },
    {
        "name": 'actor5',
        "gender": 'M',
        "date_of_birth": date(1990, 12, 3),
        "born_in_country": "country4",

    },
    {
        "name": 'actor6',
        "gender": 'F',
        "date_of_birth": date(1996, 6, 13),
        "born_in_country": "country5",

    },
    {
        "name": 'actor7',
        "gender": 'M',
        "date_of_birth": date(1970, 7, 19),
        "born_in_country": "country6",

    },
    {
        "name": 'actor8',
        "gender": 'F',
        "date_of_birth": date(1993, 2, 12),
        "born_in_country": "country2",

    },
    {
        "name": 'actor9',
        "gender": 'M',
        "date_of_birth": date(1990, 12, 3),
        "born_in_country": "country4",

    },
    {
        "name": 'actor10',
        "gender": 'M',
        "date_of_birth": date(1993, 2, 12),
        "born_in_country": "country8",

    },
    {
        "name": 'actor11',
        "gender": 'F',
        "date_of_birth": date(1996, 6, 13),
        "born_in_country": "country9",

    },
    {
        "name": 'actor12',
        "gender": 'F',
        "date_of_birth": date(1998, 9, 13),
        "born_in_country": "country2",

    },
    {
        "name": 'actor13',
        "gender": 'M',
        "date_of_birth": date(1971, 8, 20),
        "born_in_country": "country1",
    },
    {
        "name": 'actor14',
        "gender": 'F',
        "date_of_birth": date(1982, 3, 1),
        "born_in_country": "country6",

    },
    {
        "name": 'actor15',
        "gender": 'M',
        "date_of_birth": date(1964, 11, 2),
        "born_in_country": "country8",

    },
    {
        "name": 'actor16',
        "gender": 'M',
        "date_of_birth": date(1965, 2, 12),
        "born_in_country": "country3",

    },
    {
        "name": 'actor17',
        "gender": 'F',
        "date_of_birth": date(1992, 3, 13),
        "born_in_country": "country6",

    },
    {
        "name": 'actor18',
        "gender": 'F',
        "date_of_birth": date(1999, 6, 13),
        "born_in_country": "country2",

    },
    {
        "name": 'actor19',
        "gender": 'M',
        "date_of_birth": date(1971, 7, 19),
        "born_in_country": "country4",

    },
    {
        "name": 'actor20',
        "gender": 'F',
        "date_of_birth": date(1992, 4, 12),
        "born_in_country": "country5",

    },
    {
        "name": 'actor21',
        "gender": 'M',
        "date_of_birth": date(1997, 7, 3),
        "born_in_country": "country6",

    },
    {
        "name": 'actor22',
        "gender": 'M',
        "date_of_birth": date(1993, 1, 12),
        "born_in_country": "country3",

    },
    {
        "name": 'actor23',
        "gender": 'F',
        "date_of_birth": date(1992, 12, 13),
        "born_in_country": "country2",

    },
    {
        "name": 'actor24',
        "gender": 'M',
        "date_of_birth": date(1996, 5, 3),
        "born_in_country": "country3",

    },
    {
        "name": 'actor25',
        "gender": 'F',
        "date_of_birth": date(1992, 5, 13),
        "born_in_country": "country1",
    },
]

MOVIE = [
    {
        "title": "Titanic",
        "date_of_release": date(2000, 12, 4),
    },
    {
        "title": "Avatar",
        "date_of_release": date(2011, 2, 6),
    },
    {
        "title": "Avengers Endgame",
        "date_of_release": date(2015, 12, 6),
    },
    {
        "title": "Inception",
        "date_of_release": date(2014, 7, 2),
    },
    {
        "title": "Clash of the Titans",
        "date_of_release": date(2016, 11, 10),
    },
    {
        "title": "Spider Man",
        "date_of_release": date(2012, 9, 12),
    },
    {
        "title": "Iron Man",
        "date_of_release": date(2008, 3, 2),
    },
    {
        "title": "Ant Man",
        "date_of_release": date(2016, 5, 6),
    },
    {
        "title": "Bolt",
        "date_of_release": date(2017, 12, 9),
    },
    {
        "title": "Ready Player One",
        "date_of_release": date(2012, 8, 8),
    }
]

MOVIE_CAST = [
    {
        "title": "Titanic",
        "name": "actor1",
        "role": "role1",
        "remuneration_in_usd": 50000,
    },
    {
        "title": "Titanic",
        "name": "actor1",
        "role": "role2",
        "remuneration_in_usd": 25000,
    },
    {
        "title": "Titanic",
        "name": "actor2",
        "role": "role3",
        "remuneration_in_usd": 150000,
    },
    {
        "title": "Titanic",
        "name": "actor3",
        "role": "role4",
        "remuneration_in_usd": 80000,
    },
    {
        "title": "Titanic",
        "name": "actor18",
        "role": "role27",
        "remuneration_in_usd": 134000,
    },
    {
        "title": "Titanic",
        "name": "actor17",
        "role": "role28",
        "remuneration_in_usd": 80500,
    },
    {
        "title": "Titanic",
        "name": "actor11",
        "role": "role29",
        "remuneration_in_usd": 80000,
    },
    {
        "title": "Avatar",
        "name": "actor8",
        "role": "role5",
        "remuneration_in_usd": 100000,
    },
    {
        "title": "Avatar",
        "name": "actor7",
        "role": "role6",
        "remuneration_in_usd": 120000,
    },
    {
        "title": "Avatar",
        "name": "actor7",
        "role": "role7",
        "remuneration_in_usd": 80000,
    },
    {
        "title": "Avatar",
        "name": "actor10",
        "role": "role30",
        "remuneration_in_usd": 67000,
    },
    {
        "title": "Avatar",
        "name": "actor2",
        "role": "role31",
        "remuneration_in_usd": 12300,
    },
    {
        "title": "Avatar",
        "name": "actor5",
        "role": "role5",
        "remuneration_in_usd": 123500,
    },
    {
        "title": "Avengers Endgame",
        "name": "actor6",
        "role": "role8",
        "remuneration_in_usd": 97652,
    },
    {
        "title": "Avengers Endgame",
        "name": "actor16",
        "role": "role31",
        "remuneration_in_usd": 97252,
    },
    {
        "title": "Avengers Endgame",
        "name": "actor15",
        "role": "role32",
        "remuneration_in_usd": 97652,
    },
    {
        "title": "Avengers Endgame",
        "name": "actor11",
        "role": "role9",
        "remuneration_in_usd": 134567,
    },
    {
        "title": "Ant Man",
        "name": "actor2",
        "role": "role10",
        "remuneration_in_usd": 123450,
    },
    {
        "title": "Ant Man",
        "name": "actor5",
        "role": "role11",
        "remuneration_in_usd": 120000,
    },
    {
        "title": "Ant Man",
        "name": "actor9",
        "role": "role12",
        "remuneration_in_usd": 134500,
    },
    {
        "title": "Ant Man",
        "name": "actor14",
        "role": "role32",
        "remuneration_in_usd": 13500,
    },
    {
        "title": "Ant Man",
        "name": "actor19",
        "role": "role33",
        "remuneration_in_usd": 13400,
    },
    {
        "title": "Bolt",
        "name": "actor8",
        "role": "role13",
        "remuneration_in_usd": 123400,
    },
    {
        "title": "Bolt",
        "name": "actor11",
        "role": "role34",
        "remuneration_in_usd": 123600,
    },
    {
        "title": "Bolt",
        "name": "actor17",
        "role": "role35",
        "remuneration_in_usd": 34400,
    },
    {
        "title": "Spider Man",
        "name": "actor1",
        "role": "role14",
        "remuneration_in_usd": 90000,
    },
    {
        "title": "Spider Man",
        "name": "actor5",
        "role": "role15",
        "remuneration_in_usd": 57000,
    },
    {
        "title": "Spider Man",
        "name": "actor10",
        "role": "role36",
        "remuneration_in_usd": 57450,
    },
    {
        "title": "Inception",
        "name": "actor5",
        "role": "role16",
        "remuneration_in_usd": 64000,
    },
    {
        "title": "Inception",
        "name": "actor2",
        "role": "role17",
        "remuneration_in_usd": 123000,
    },
    {
        "title": "Inception",
        "name": "actor4",
        "role": "role18",
        "remuneration_in_usd": 12100,
    },
    {
        "title": "Clash of the Titans",
        "name": "actor4",
        "role": "role19",
        "remuneration_in_usd": 122334,
    },
    {
        "title": "Clash of the Titans",
        "name": "actor6",
        "role": "role20",
        "remuneration_in_usd": 123987,
    },
    {
        "title": "Iron Man",
        "name": "actor10",
        "role": "role21",
        "remuneration_in_usd": 90876,
    },
    {
        "title": "Iron Man",
        "name": "actor10",
        "role": "role22",
        "remuneration_in_usd": 90876,
    },
    {
        "title": "Iron Man",
        "name": "actor3",
        "role": "role23",
        "remuneration_in_usd": 123450,
    },
    {
        "title": "Ready Player One",
        "name": "actor7",
        "role": "role24",
        "remuneration_in_usd": 12876,
    },
    {
        "title": "Ready Player One",
        "name": "actor5",
        "role": "role25",
        "remuneration_in_usd": 90806,
    },
    {
        "title": "Ready Player One",
        "name": "actor11",
        "role": "role26",
        "remuneration_in_usd": 70876,
    },
]

MOVIE_RATING = [
    {
        "title": "Titanic",
        "rating": 1,
        "no_of_ratings": 2000,
    },
    {
        "title": "Titanic",
        "rating": 2,
        "no_of_ratings": 1000,
    },
    {
        "title": "Titanic",
        "rating": 3,
        "no_of_ratings": 4000,
    },
    {
        "title": "Titanic",
        "rating": 4,
        "no_of_ratings": 10000,
    },
    {
        "title": "Titanic",
        "rating": 5,
        "no_of_ratings": 20000,
    },
    {
        "title": "Ready Player One",
        "rating": 1,
        "no_of_ratings": 9000,
    },
    {
        "title": "Ready Player One",
        "rating": 3,
        "no_of_ratings": 12000,
    },
    {
        "title": "Ready Player One",
        "rating": 5,
        "no_of_ratings": 20000,
    },
    {
        "title": "Iron Man",
        "rating": 1,
        "no_of_ratings": 100,
    },
    {
        "title": "Iron Man",
        "rating": 2,
        "no_of_ratings": 1000,
    },
    {
        "title": "Iron Man",
        "rating": 4,
        "no_of_ratings": 20000,
    },
    {
        "title": "Iron Man",
        "rating": 5,
        "no_of_ratings": 19000,
    },
    {
        "title": "Clash of the Titans",
        "rating": 1,
        "no_of_ratings": 2000,
    },
    {
        "title": "Clash of the Titans",
        "rating": 2,
        "no_of_ratings": 2000,
    },
    {
        "title": "Clash of the Titans",
        "rating": 5,
        "no_of_ratings": 21900,
    },
    {
        "title": "Ant Man",
        "rating": 1,
        "no_of_ratings": 100,
    },
    {
        "title": "Ant Man",
        "rating": 3,
        "no_of_ratings": 20000,
    },
    {
        "title": "Spider Man",
        "rating": 1,
        "no_of_ratings": 1040,
    },
    {
        "title": "Spider Man",
        "rating": 5,
        "no_of_ratings": 21230,
    },
    {
        "title": "Inception",
        "rating": 1,
        "no_of_ratings": 1000,
    },
    {
        "title": "Inception",
        "rating": 2,
        "no_of_ratings": 12000,
    },
    {
        "title": "Inception",
        "rating": 3,
        "no_of_ratings": 12000,
    },
    {
        "title": "Inception",
        "rating": 4,
        "no_of_ratings": 18000,
    },
    {
        "title": "Inception",
        "rating": 5,
        "no_of_ratings": 17000,
    },
    {
        "title": "Bolt",
        "rating": 1,
        "no_of_ratings": 2000,
    },
    {
        "title": "Bolt",
        "rating": 2,
        "no_of_ratings": 2000,
    },
    {
        "title": "Bolt",
        "rating": 3,
        "no_of_ratings": 2000,
    },
    {
        "title": "Bolt",
        "rating": 4,
        "no_of_ratings": 2000,
    },
    {
        "title": "Bolt",
        "rating": 5,
        "no_of_ratings": 2000,
    },
]


def create_actor(data):
    for each_item in data:
        Actor.objects.create(name=each_item['name'], gender=each_item['gender'],
                             date_of_birth=each_item['date_of_birth'], unique_id=str(uuid.uuid4()),
                             born_in_country=each_item['born_in_country'])


def create_movie(data):
    for each_item in data:
        Movie.objects.create(title=each_item['title'], date_of_release=each_item['date_of_release'])
    pass


def create_movie_cast(data):
    for each_item in data:
        movie = Movie.objects.get(title=each_item['title'])
        actor = Actor.objects.get(name=each_item['name'])
        MovieCast.objects.create(movie=movie, cast=actor, role=each_item['role'],
                                 remuneration_in_usd=each_item['remuneration_in_usd'])
    pass


def create_movie_rating(data):
    for each_item in data:
        movie = Movie.objects.get(title=each_item['title'])
        MovieRating.objects.create(movie=movie, rating=each_item['rating'], no_of_ratings=each_item['no_of_ratings'])
    pass


def populate(check_id):
    if check_id == 1:
        create_actor(ACTOR)
    elif check_id == 2:
        create_movie(MOVIE)
    elif check_id == 3:
        create_movie_cast(MOVIE_CAST)
    elif check_id == 4:
        create_movie_rating(MOVIE_RATING)
    else:
        return 'Invalid check_id'
