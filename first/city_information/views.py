from django.shortcuts import render
from .models import *
from django.core.exceptions import *
from django.db.models import *


class CityException(Exception):
    def __init__(self, error):
        self.error = error


def get_cities():
    cities = City.objects.filter(country_code='country_code1', population__gt=234)
    return cities


def get_all_cities():
    cities = City.objects.all()
    return cities


def get_city_using_id(input_id):
    try:
        city = City.objects.get(id=input_id)
        return city
    except ObjectDoesNotExist:
        raise CityException('City Object Does Not Found')


def get_cities_by_country_code(country_code):
    cities = City.objects.filter(country_code=country_code)
    return cities


def get_city_names_by_country_code(country_code):
    city_names = City.objects.filter(country_code=country_code).values('name')
    return city_names


def get_station_and_cities():
    city_with_state = City.objects.all().annotate(state=F('state_details__state'), lat_n=F('state_details__lat_n'),
                                                  long_w=F('state_details__long_w'))
    city_with_state[1].long_w
    return city_with_state
