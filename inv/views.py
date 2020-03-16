from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
from users.models import CustomUser

from django.shortcuts import render
from django.http import HttpResponse

from .models import Item
from .forms import BarcodeForm, ModifyDevice
from dev.models import Device, ObjType



def index(request):
    
    #if they are NOT loggedin...
    if not request.user.is_authenticated:
        context = {
            "state": "home"
            }
        return render(request, "inv/index.html", context)


    #otherwise, if they are logged in...
    username = request.user
    userid = username.id
    form = BarcodeForm()

    context = {
        "state": "loggedin",
        "first": username.first_name,
        "error": "",
        "form": form
    }

    return render(request,"inv/index.html",context)

#send user to login form
def login_form(request):
    context = {
            "state": "login",
            "error": ""
        }
    return render(request, "inv/index.html", context)


#log user in
def login_view(request):
    username = request.POST["inputUsername"]
    password = request.POST["inputPassword"]

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        context = {
            "state": "login",
            "error": "Invalid credentials, try again."
            }
        return render(request, "inv/index.html", context)


#log user out
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))



def barcode(request,barcode):
    context = {}
    return render(request,"inv/type.html",context)


# view a device and its components
def item_view(request):
    barcode = request.POST["inputBarcode"]
    print(barcode)
        #if they are NOT loggedin...
    if not request.user.is_authenticated:
        context = {
            "state": "home",
            "error": "Please login and try again."
            }
        return render(request, "inv/index.html", context)

    #otherwise, if they are logged in...
    username = request.user
    userid = username.id

    try:

        item = Item.objects.get(barcode=barcode)

        context = {
            "item" : item
        }

        return render(request, "inv/item.html", context)


    except Item.DoesNotExist:

        context = {
            "state": "loggedin",
            "error": "Item "+barcode+" not found, try again."
            }
        return render(request, "inv/index.html", context)


def modify(request):

    # try: 
    #     if request.method == 'POST' and request.FILES['myfile']:


    #         myfile = request.FILES['myfile']
    #         fs = FileSystemStorage()
    #         filename = fs.save(myfile.name, myfile)
    #         print(myfile.name) #<-- change filename
    #         uploaded_file_url = fs.url(filename)


    #         itemid = request.POST["itemid"]
    #         item = Item.objects.get(id=itemid)

    #         context = {
    #                     "uploaded_file_url": uploaded_file_url,
    #                     "item" : item
    #         } 

    #         return render(request, 'inv/modify.html', context )
    # except:
    #     pass




    comps = request.POST.getlist('components')
    print(comps)
    for x in comps:
        print(x)



    itemid = request.POST["itemid"]

    if not request.user.is_authenticated:
        context = {
            "state": "home",
            "error": "Please login and try again."
            }
        return render(request, "inv/index.html", context)

    try:

        item = Item.objects.get(id=itemid)

        form = ModifyDevice()

        context = {
            "item" : item,
            "form" : form,
        }

        return render(request, "inv/modify.html", context)


    except Item.DoesNotExist:

        context = {
            "state": "loggedin",
            "error": "Item "+barcode+" not found, try again."
            }
        return render(request, "inv/index.html", context)


def upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'inv/model_form_upload.html', {
        'form': form
    })



def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:

        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        itemid = request.POST["itemid"]
        item = Item.objects.get(id=itemid)

        context = {
                    "uploaded_file_url": uploaded_file_url,
                    "item" : item
        } 

        return render(request, 'inv/modify.html', context )

    return render(request, 'inv/modify.html')


# check in device, not used not finished
def check_in(request):
    status = request.POST["status"]
    itemid = request.POST["itemid"]
    print(status)
        #if they are NOT loggedin...
    if not request.user.is_authenticated:
        context = {
            "state": "home",
            "error": "Please login and try again."
            }
        return render(request, "inv/index.html", context)

    #otherwise, if they are logged in...
    username = request.user
    userid = username.id

    try:

        item = Item.objects.get(id=itemid)

        context = {
            "item" : item,
            "state" : status
        }

        return render(request, "inv/checkin.html", context)


    except Item.DoesNotExist:

        context = {
            "state": "loggedin",
            "error": "Item "+barcode+" not found, try again."
            }
        return render(request, "inv/index.html", context)



# def devname(request,devname):
#     context = {}
#     return render(request,"dev/device.html",context)