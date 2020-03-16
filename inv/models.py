from django.db import models
from users.models import CustomUser
from dev.models import Device


class Component(models.Model):
    component = models.CharField(max_length=50,null=True, blank=True)
    img = models.CharField(max_length=20,null=True, blank=True)

    def __str__(self):
        return f"{self.component}"

class Cleaning(models.Model):
    cleaning = models.CharField(max_length=50,null=True, blank=True)
    img = models.CharField(max_length=20,null=True, blank=True)

    def __str__(self):
        return f"{self.cleaning}"

class Checking(models.Model):
    checking = models.CharField(max_length=250,null=True, blank=True)
    img = models.CharField(max_length=20,null=True, blank=True)

    def __str__(self):
        return f"{self.checking}"

class Location(models.Model):
    location = models.CharField(max_length=50,null=True, blank=True)
    img = models.CharField(max_length=20,null=True, blank=True)

    def __str__(self):
        return f"{self.location}"


class Item(models.Model):
    name = models.ForeignKey(Device, on_delete=models.CASCADE, null=True, blank=True)
    barcode = models.CharField(max_length=20,null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    components = models.ManyToManyField(Component, blank=True)
    cleaning = models.ManyToManyField(Cleaning, blank=True)
    checking = models.ManyToManyField(Checking, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"



#attempts at working with file uploads

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='media/')
    uploaded_at = models.DateTimeField(auto_now_add=True)



# dont need anything below probably

class Status(models.Model):
    status = models.CharField(max_length=50,null=True, blank=True)
    # ok, damaged, missing componets, lost device  
    def __str__(self):
        return f"{self.status}"


class CheckIn(models.Model):

    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True) #record created date
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.date}: {self.item}"





"""
item
component
status


"""