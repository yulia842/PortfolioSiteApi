from rest_framework import viewsets 
from rest_framework.decorators import action
from .models import Joke, Location
from .serializers import  JokeSerializer, LocationSerializer
from rest_framework.response import Response
from random import choice

class JokeViewSet(viewsets.ModelViewSet):
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer

    @action(methods=['GET'], detail=False)
    def generate(self, request):
        queryset = self.get_queryset()
        random_joke = choice(queryset)
        serializer = self.get_serializer(random_joke)
        return Response(serializer.data)
    
class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
