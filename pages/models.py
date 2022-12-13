from django.db import models
from datetime import datetime, timedelta
from django import forms

            
 # Create your models here.
class Review(models.Model):
    reviewer_name = models.CharField("User Name", default='', max_length=30)
    cruise_choices = [
        ('Carnival', 'Carnival'),
        ('Celestyal', 'Celestyal'),
        ('Costa', 'Costa'),
        ('Disney', 'Disney'),
        ('MSC', 'MSC'),
        ('Norwegian', 'Norwegian'),
        ('Princess', 'Princess'),
        ('Royal Carribean International', 'Royal Carribean International'),
        ('Virgin Voyages', 'Virgin Voyages'),
        ('Azamara', 'Azamara'),
        ('Celebrity', 'Celebrity'),
        ('Holland America', 'Holland America'),
        ('Oceania', 'Oceania'),
        ('Viking', 'Viking'),
        ('Cunard', 'Cunard'),
        ('Regent Seven Seas', 'Regent Seven Seas'),
        ('Seabourn', 'Seabourn'),
        ('Sea Dream', 'Sea Dream'),
        ('Silversea', 'Silversea'),
        ('Swan Hellenic', 'Swan Hellenic'),
        ('Windstar', 'Windstar')
    ]
    cruise_liner_name = models.CharField("Cruise Line", default="Carnival", max_length=30, choices=cruise_choices)
    ship_name = models.CharField("Ship Name", null=True, max_length=30)
    general_location = models.CharField("General Location", null=True, max_length=30)
    month_choices = [
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
        (6,6),
        (7,7),
        (8,8),
        (9,9),
        (10,10),
        (11,11),
        (12,12),
    ]
    month = models.CharField("Month", null=True, max_length=10, choices=month_choices)
    length_in_days = models.IntegerField("Length of Trip (in days)", null=True)
    star_choices = [
        (1,1),
        (2,2),
        (3,3),
        (5,5),
        (4,4)
        
    ]
    star_rating = models.IntegerField("Star Rating", default=3, choices=star_choices)
    comments = models.CharField("Comments", null=True, max_length=255)

    def __str__(self):
        return (self.reviewer_name)

    class Meta:
        db_table = 'review'