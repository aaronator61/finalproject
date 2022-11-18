from django.contrib import admin
from .models import CruiseLine, Ship, Trip, User, Review

# Register your models here.
admin.site.register(CruiseLine)
admin.site.register(Ship)
admin.site.register(Trip)
admin.site.register(User)
admin.site.register(Review)