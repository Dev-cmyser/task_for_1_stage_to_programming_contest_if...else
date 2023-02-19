from rest_framework import serializers


from .models import  AnimalTypes, VisitedLocations, Animal, Location

class AnimalTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalTypes
        fields = '__all__'
        
        
class VisitedLocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitedLocations
        fields = '__all__'
        
        
class AnimalSerializer(serializers.ModelSerializer):

    animal_types = AnimalTypesSerializer(source='animaltypes_set', many=True)
    class Meta:
        model = Animal
        fields = '__all__'
        
        
class LocationSerializer(serializers.ModelSerializer):

    visited_locations = VisitedLocationsSerializer(source='visitedlocations_set', many=True)
    class Meta:
        model = Location
        fields = '__all__'