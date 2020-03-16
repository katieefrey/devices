from django.db import models
from users.models import CustomUser

class ObjType(models.Model):

    objtype = models.CharField(max_length=50)
    name = models.CharField(max_length=50,null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

class Device(models.Model):

    name = models.CharField(max_length=20)
    fullname = models.CharField(max_length=50,null=True, blank=True)
    hollis = models.CharField(max_length=30,null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    shortdesc = models.CharField(max_length=200,null=True, blank=True)
    date = models.DateField()
    url = models.CharField(max_length=200,null=True, blank=True)
    objtype = models.ForeignKey(ObjType, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.objtype}: {self.fullname}"
