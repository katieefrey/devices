import requests
import json

from django.shortcuts import render
from django.http import HttpResponse

from .models import ObjType, Device


def checkforlist(thing):
    if type(thing) == list:
        return thing
    else:
        newthing = [thing]
        return newthing

def index(request):
    
    all_types = ObjType.objects.all().order_by('name')

    all_devices = Device.objects.order_by('-date').all()

    context = { "types"     :   all_types,
                "devices"   :   all_devices,
                "objtype"   :   "",
            }

    return render(request,"dev/type.html",context)


def typepage(request,typepage):

    all_types = ObjType.objects.all().order_by('name')
    thisobj = ObjType.objects.get(objtype=typepage)
    objlist = Device.objects.filter(objtype=thisobj.id).order_by('-date')

    context = { "types"     :   all_types,
                "devices"   :   objlist,
                "objtype"   :   typepage,
            }

    return render(request,"dev/type.html",context)


def devname(request,devname):

    all_types = ObjType.objects.all().order_by('name')
    device = Device.objects.get(name=devname)

    url = "http://webservices.lib.harvard.edu/rest/avail/hollis/"+device.hollis+"?jsonp=result"
    content = requests.get(url)
    k = json.loads(content.text[7:-2])

    item = k["availability"]["items"]["item"]

    itemlist = checkforlist(item)

    for x in itemlist:
        if "WOL" in x['library']:
            status = x["status"]
            nonAvail = x["nonAvail"]
            totalItems =x["totalItems"]

            numAvail = totalItems - nonAvail

            if numAvail == 0:
                availphrase = "currently unavailable"
            elif numAvail > 0:
                availphrase = "<strong>avaialble</strong> for checkout"
            else:
                availphrase = "cannot determine availability"
        
        else:
            availphrase = "cannot determine availability"

        context = { "types"     :   all_types,
                    "device"    :   device,
                    "availphrase" : availphrase,
                }

    return render(request,"dev/device.html",context)