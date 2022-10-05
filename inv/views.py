from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
from users.models import CustomUser

from django.shortcuts import render
from django.http import HttpResponse

from .models import Item
from .forms import BarcodeForm, ModifyDevice, DevComp, DevCheck, DevClean, DevLoc, ChoiceForm
from dev.models import Device, ObjType
from inv.models import Cleaning, Checking, Component



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



# view a device and its components
def item_view(request):
    barcode = request.POST["inputBarcode"]

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


    itemid = request.POST["itemid"]

    if not request.user.is_authenticated:
        context = {
            "state": "home",
            "error": "Please login and try again."
            }
        return render(request, "inv/index.html", context)

    try:

        item = Item.objects.get(id=itemid)

        compform = DevComp(instance=Item.objects.get(id=itemid))
        cleanform = DevClean(instance=Item.objects.get(id=itemid))
        checkform = DevCheck(instance=Item.objects.get(id=itemid))
        locform = DevLoc(instance=Item.objects.get(id=itemid))

        choicetest = ChoiceForm(instance=Item.objects.get(id=itemid))

        context = {
            "item" : item,
            "compform" : compform,
            "cleanform" : cleanform,
            "checkform" : checkform,
            "locform" : locform,
            "choiceform" : choicetest,
        }

        return render(request, "inv/modify.html", context)


    except Item.DoesNotExist:

        context = {
            "state": "loggedin",
            "error": "Item "+barcode+" not found, try again."
            }
        return render(request, "inv/index.html", context)


def add_dev(request):

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


    # itemid = request.POST["itemid"]

    if not request.user.is_authenticated:
        context = {
            "state": "home",
            "error": "Please login and try again."
            }
        return render(request, "inv/index.html", context)

    try:

        items = Device.objects.all()


        # item = Item.objects.get(id=itemid)



        compform = DevComp()
        cleanform = DevClean()
        checkform = DevCheck()
        locform = DevLoc()

        choicetest = ChoiceForm()

        context = {
            "items" : items,
            "compform" : compform,
            "cleanform" : cleanform,
            "checkform" : checkform,
            "locform" : locform,
            "choiceform" : choicetest,
        }

        return render(request, "inv/add.html", context)


    except Item.DoesNotExist:

        context = {
            "state": "loggedin",
            "error": "Item "+barcode+" not found, try again."
            }
        return render(request, "inv/index.html", context)

def update(request):

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

        comps = request.POST.getlist('components')
        checks = request.POST.getlist('checking')
        cleans = request.POST.getlist('cleaning')

        loc = request.POST["location"]
        itemid = request.POST["itemid"]

        myItem = Item.objects.get(id=itemid)
        
        myItem.checking.clear()
        for x in checks:
            myItem.checking.add(x)

        myItem.components.clear()
        for x in comps:
            myItem.components.add(x)

        myItem.cleaning.clear()
        for x in cleans:
            myItem.cleaning.add(x)

        myItem.location_id = loc

        myItem.save()

        context = {
            "item" : myItem
        }

        return render(request, "inv/item.html", context)
        #return HttpResponseRedirect(reverse("item_view"))
        #return HttpResponseRedirect('batch/%s' % batchid)

    except Item.DoesNotExist:

        context = {
            "state": "loggedin",
            "error": "Item not found, try again."
            }
        return render(request, "inv/index.html", context)


def add_item(request):

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

        comps = request.POST.getlist('components')
        checks = request.POST.getlist('checking')
        cleans = request.POST.getlist('cleaning')

        loc = request.POST["location"]
        notes = request.POST["notes"]
        itemid = request.POST["itemid"]

        print(notes)

        print (request)

        deviceid = request.POST["device_id"]

        print(deviceid)

        barcode = request.POST["barcode"]
        print (barcode)
        
        myItem = Item.objects.create(barcode=barcode)
        
        myItem.checking.clear()
        for x in checks:
            myItem.checking.add(x)

        myItem.components.clear()
        for x in comps:
            myItem.components.add(x)

        myItem.cleaning.clear()
        for x in cleans:
            myItem.cleaning.add(x)

        myItem.location_id = loc
        myItem.notes = notes
        myItem.name_id = deviceid

        myItem.save()

        context = {
            "item" : myItem
        }

        return render(request, "inv/item.html", context)
        #return HttpResponseRedirect(reverse("item_view"))
        #return HttpResponseRedirect('batch/%s' % batchid)

    except Item.DoesNotExist:

        context = {
            "state": "loggedin",
            "error": "Item not found, try again."
            }
        return render(request, "inv/index.html", context)

def add_comp(request):

    if request.POST:

        print("post request!")

        comp = request.POST.get("tocomp")
        print(comp)

        component = Component.objects.all()

        newC = Component.objects.create(component=comp)
        newC.save()

        context = {
            "component" : component,
        }
        return render(request, "inv/add_comp.html", context)

    else:

            component = Component.objects.all()
            context = {
                "component" : component,
            }
            return render(request, "inv/add_comp.html", context)


def add_clean(request):

    if request.POST:

        print("post request!")

        clean = request.POST.get("toclean")
        print(clean)

        cleaning = Cleaning.objects.all()

        newCL = Cleaning.objects.create(cleaning=clean)
        newCL.save()

        context = {
            "cleaning" : cleaning,
        }
        return render(request, "inv/add_cl.html", context)

    else:

        cleaning = Cleaning.objects.all()
        context = {
            "cleaning" : cleaning,
        }
        return render(request, "inv/add_cl.html", context)

def add_check(request):

    if request.POST:

        print("post request!")

        check = request.POST.get("tocheck")
        print(check)

        checking = Checking.objects.all()

        newCH = Checking.objects.create(checking=check)
        newCH.save()

        context = {
            "checking" : checking,
        }
        return render(request, "inv/add_ch.html", context)

    else:

        checking = Checking.objects.all()
        context = {
            "checking" : checking,
        }
        return render(request, "inv/add_ch.html", context)


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