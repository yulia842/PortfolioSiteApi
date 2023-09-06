from rest_framework import serializers
from .models import Location, Joke

class JokeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Joke
        fields = "__all__"

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"