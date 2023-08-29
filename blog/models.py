from django.db import models

class Joke(models.Model):
    joke = models.TextField(max_length=600)

class Location(models.Model):
    location = models.CharField(max_length=100)
    latitude = models.IntegerField(max_length=20)
    longitude = models.IntegerField(max_length=20)