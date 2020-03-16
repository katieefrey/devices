from django.contrib import admin

from .models import Component, Cleaning, Checking, Location, Item, Status, CheckIn

# Register your models here.
admin.site.register(Component)
admin.site.register(Cleaning)
admin.site.register(Checking)
admin.site.register(Location)
admin.site.register(Item)
admin.site.register(Status)
admin.site.register(CheckIn)