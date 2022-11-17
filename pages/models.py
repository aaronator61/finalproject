from django.db import models
from datetime import datetime, timedelta
            
 # Create your models here.
class CruiseLine(models.Model):
    CruiseLineName = models.CharField(max_length=30)
    
    def __str__(self) :
        return (self.CruiseLineName)
            
#changed class name
class Ship(models.Model) :
    cruise_line = models.ForeignKey(CruiseLine, models.CASCADE)
    ship_name = models.CharField(max_length=50)

    def __str__ (self):
        return (self.ship_name)

class Trip(models.Model):
    location = models.CharField(max_length=50)
    start_date = models.DateField(default=datetime.today, blank=True)
    trip_length = models.IntegerField(default=0)
    ship = models.ManyToManyField(Ship, blank=True)

    @property
    def return_date(self) :
        return (self.start_date + timedelta(days=self.trip_length))

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return (self.username)
    
    #override the save method
    def save(self):
        super(User, self).save() # Call the "real" save() method.

class Review(models.Model) :
    trip = models.ForeignKey(Trip, models.CASCADE)
    user = models.ForeignKey(User, models.CASCADE)
    Rating = models.IntegerField(default=0)
    description = models.CharField(max_length=150)
