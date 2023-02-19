from rest_framework import viewsets
from .models import   Animal, Location

from .serializers import LocationSerializer, AnimalSerializer 



class AnimalView(viewsets.ModelViewSet):
    serializer_class = AnimalSerializer
    queryset = Animal.objects.all()


class LocationView(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()




    