from django.db import models


class Station(models.Model):
    state = models.CharField(max_length=4)
    lat_n = models.IntegerField()
    long_w = models.IntegerField()

    def __str__(self):
        return self.state


class City(models.Model):
    name = models.CharField(max_length=17)
    country_code = models.CharField(max_length=3)
    district = models.CharField(max_length=23)
    population = models.IntegerField(default=0)
    state_details = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='cities', related_query_name='city')

    def __str__(self):
        return self.name
