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
    
    all_types = ObjType.objects.all().order_by('order')

    all_devices = Device.objects.order_by('-date').filter(show=1)

    context = { "types"     :   all_types,
                "devices"   :   all_devices,
                "objtype"   :   "",
            }

    return render(request,"dev/type.html",context)


def typepage(request,typepage):

    all_types = ObjType.objects.all().order_by('order')
    thisobj = ObjType.objects.get(objtype=typepage)
    objlist = Device.objects.filter(objtype=thisobj.id, show=1).order_by('-date')

    context = { "types"     :   all_types,
                "devices"   :   objlist,
                "objtype"   :   typepage,
                "type"      :   thisobj.name,
            }

    return render(request,"dev/type.html",context)


def devname(request,devname):

    all_types = ObjType.objects.all().order_by('order')

    try: 
        device = Device.objects.get(name=devname)

        print(device)

        context = { "types"     :   all_types,
                    "device"    :   device
                }

        print (context)

        return render(request,"dev/device.html",context)

    except:

        all_devices = Device.objects.order_by('-date').all()

        context = { "types"     :   all_types,
                    "devices"   :   all_devices,
                    "objtype"   :   "",
                }        

        return render(request, "dev/type.html", context)


def borrowingpolicy(request):
    
    all_types = ObjType.objects.all().order_by('order')

    all_devices = Device.objects.order_by('-date').all()

    context = { "types"     :   all_types,
                "devices"   :   all_devices,
                "objtype"   :   "",
            }

    return render(request,"dev/borrowingpolicy.html",context)