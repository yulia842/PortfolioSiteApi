from django.db import models


class Joke(models.Model):
    joke = models.TextField(max_length=600)


class Location(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.IntegerField()
    longitude = models.IntegerField()
    expirence = models.TextField(max_length=600)
