from django.contrib import admin

from .models import ObjType, Device

# Register your models here.
admin.site.register(ObjType)
admin.site.register(Device)
