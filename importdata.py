# standard lib packages
import sys
import os
import json
import time
import csv

os.environ.setdefault('DJANGO_SETTINGS_MODULE','devices.settings')

import django
django.setup()

from dev.models import Device, ObjType
from inv.models import Inventory, Component, Proceedure


def add_Device(data1, data2, data3, data4, data5, data6, data7, data8):
    d, created = Device.objects.get_or_create(name=data1, hollis=data2, fullname=data3, desc=data4, shortdesc=data5, date=data6, url=data7, objtype_id=data8)

    return d

def add_Inventory(data1, data2, data3, data4, data5, data6, data7, data8):
    d, created = Device.objects.get_or_create(name=data1, barcode=data2, notes=data3)

    return d


with open('devices.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row)
        print(row[7])

        obj = ObjType.objects.get(objtype=row[7])
        print(obj.id)

        #add_Device(row[0],row[1],row[2],row[3],row[4],row[5],row[6],obj.id)



with open('devinv.csv') as csv_file2:
    csv_reader2 = csv.reader(csv_file2, delimiter=',')
    for row in csv_reader2:

        add_Inventory(name, barcode, notes)
