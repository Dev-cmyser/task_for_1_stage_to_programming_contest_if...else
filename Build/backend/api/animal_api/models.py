import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.functions import Cast
import datetime

# Create your models here

class BaseModel(models.Model):
    """Basic Model"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at', '-updated_at']


class User(AbstractUser):
    firstName = models.CharField(max_length=255, blank=True, null=True, verbose_name="first name")
    lastName = models.CharField(max_length=255, blank=True, null=True, verbose_name="last name")
    email = models.EmailField(max_length=255, blank=True, null=True, unique=True, verbose_name="email")
    password = models.CharField(max_length=100, verbose_name="password")
    from_start = models.IntegerField(default=0, blank=True, null=True, verbose_name="count from start")
    size = models.IntegerField(default=0, blank=True, null=True, verbose_name="size")
    
    def __str__(self):
        return f'{self.firstName}, {self.lastName}, {self.email}'
    
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class Location(BaseModel):
    latitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="latitude")
    longitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="longiude")
    point = models.CharField(max_length=250, unique=True, blank=True, null=True, verbose_name="Point(latitude, longiude)")
    
    
    def __str__(self):
        return f'Point({self.latitude}, {self.longitude}), → unique == ({self.point})'
    
    
    def save(self, *args, **kwargs):
        self.point = f'{self.latitude}, {self.longitude}'
        super().save(*args, **kwargs)
        
        if self.point is None:
            self.point = f'{self.latitude}, {self.longitude}'
            self.save()
            
    
    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'
            
            

class Animal(BaseModel):
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    OTHER = 'OTHER'
    GENDER_CHOICES = [
        (MALE, 'MALE'),
        (FEMALE, 'FEMALE'),
        (OTHER, 'OTHER'),
    ]
    
    ALIVE = 'ALIVE'
    DEAD = 'DEAD'
    LIFA_CHOISES = [
        (ALIVE, 'ALIVE'),
        (DEAD, 'DEAD'),
    ]
    
    weight = models.FloatField(blank=True, null=True, verbose_name="weight")
    length = models.FloatField(blank=True, null=True, verbose_name="length")
    height = models.FloatField(blank=True, null=True, verbose_name="height")
    gender  = models.CharField(max_length=50, blank=True, null=True, verbose_name="gender", 
        choices=GENDER_CHOICES,
        default=OTHER)
    life_status = models.CharField(max_length=50, blank=True, null=True, verbose_name="life_status", 
        choices=LIFA_CHOISES,
        default=ALIVE)
    chipping_date_time = models.DateTimeField(auto_now=True, blank=True, null=True,  verbose_name="chipping_date_time")
    chipper_id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    chipping_location_id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    death_date_time = models.DateTimeField(default=None, blank=True, null=True,  verbose_name="death_date_time")
    
    def save(self, *args, **kwargs):
        self.death_date_time = datetime.datetime.now()
        super().save(*args, **kwargs)
        
        if self.life_status is self.DEAD:
            self.death_date_time = datetime.datetime.now()
            self.save()
            
    class Meta:
        verbose_name = 'Животное'
        verbose_name_plural = 'Животные'
        
    def __str__(self):
        return f'{self.gender}, {self.life_status}, {self.chipper_id}'

        
class VisitedLocations(BaseModel):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, null=True, blank=True, default=None)
    visited_location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True, default=None)

    
    class Meta:
        verbose_name = 'Посещенная локация'
        verbose_name_plural = 'Посещенные локации'
        
    def __str__(self):
        return f'{self.animal.chipper_id}, {self.animal.life_status}, {self.visited_location.point}'

class AnimalTypes(BaseModel):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, null=True, blank=True, default=None)
    animal_type = models.CharField(max_length=250, unique=True, blank=True, null=True, verbose_name="animal_type")
    
    class Meta:
        verbose_name = 'Тип животного'
        verbose_name_plural = 'Типы животного'
        
    def __str__(self):
        return f'{self.animal.chipper_id}, {self.animal.life_status}, {self.animal_type}'