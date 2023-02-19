from django.contrib import admin
from .models import Location, User, Animal, AnimalTypes, VisitedLocations
# Register your models here.

class LocationAdmin(admin.ModelAdmin):
    fields = ('latitude', 'longitude')


admin.site.register(Location, LocationAdmin)
admin.site.register(User)
admin.site.register(Animal)
admin.site.register(AnimalTypes)
admin.site.register(VisitedLocations)