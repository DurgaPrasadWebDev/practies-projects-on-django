from .models import *

STATE = [
    {
        "state": "A.P",
        "lat_n": 12,
        "long_w": 30,
    },
    {
        "state": "T.S",
        "lat_n": 78,
        "long_w": 90,
    },
    {
        "state": "M.P",
        "lat_n": 23,
        "long_w": 46,
    },
    {
        "state": "U.P",
        "lat_n": 7,
        "long_w": 18,
    },
]

CITY_INFORMATION = [
    {
        "name": "city1",
        "country_code": "country_code1",
        "district": "district1",
        "population": 300,
        "state": "A.P",
    },
    {
        "name": "city2",
        "country_code": "country_code1",
        "district": "district2",
        "population": 2300,
        "state": "A.P",
    },
    {
        "name": "city3",
        "country_code": "country_code3",
        "district": "district3",
        "population": 5600,
        "state": "T.S",
    },
    {
        "name": "city4",
        "country_code": "country_code4",
        "district": "district4",
        "population": 20,
        "state": "T.S",
    },
    {
        "name": "city5",
        "country_code": "country_code5",
        "district": "district5",
        "population": 323,
        "state": "M.P",
    },
    {
        "name": "city6",
        "country_code": "country_code6",
        "district": "district6",
        "population": 2340,
        "state": "M.P",
    },
    {
        "name": "city7",
        "country_code": "country_code1",
        "district": "district7",
        "population": 303,
        "state": "U.P",
    },
    {
        "name": "city8",
        "country_code": "country_code8",
        "district": "district8",
        "population": 323,
        "state": "U.P",
    },
    {
        "name": "city9",
        "country_code": "country_code9",
        "district": "district9",
        "population": 321,
        "state": "M.P",
    },
    {
        "name": "city10",
        "country_code": "country_code10",
        "district": "district10",
        "population": 123,
        "state": "A.P"
    },
    {
        "name": "city11",
        "country_code": "country_code11",
        "district": "district11",
        "population": 30,
        "state": "T.S",
    },

]


def create_state(data):
    for each_item in data:
        Station.objects.create(state=each_item['state'], lat_n=each_item['lat_n'], long_w=each_item['long_w'])


def create_city(data):
    for each_item in data:
        state = Station.objects.get(state=each_item['state'])
        City.objects.create(name=each_item['name'], country_code=each_item['country_code'],
                            district=each_item['district'], population=each_item['population'], state=state)


def populate(check_id):
    if check_id == 0:
        create_state(STATE)
    elif check_id == 1:
        create_city(CITY_INFORMATION)
    else:
        return 'invalid check_id'
