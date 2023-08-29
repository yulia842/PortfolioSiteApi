from rest_framework import serializers
from .models import Location, Joke

class JokesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Joke
        fields = "__all__"

class LocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"