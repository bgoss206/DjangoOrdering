from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Order, Sundry, Item, Equipment, Jobsite
from .forms import CreateNewOrder
from django.db.models import F
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required


def home(response):
    return render(response, "main/home.html", {})


# TODO: ENSURE THAT LOW QUANTITY ITEMS GET REORDERED 
# TODO: ADD SIDEBAR AND NAVIGATION FOR USERS WHEN THE SITE IS LOADED UP 
# TODO: FORMAT AND STYLE

@login_required
def orders(response):
    if response.method == "POST":
        form = CreateNewOrder(response.POST, sundries = Sundry.objects.all(), equipment = Equipment.objects.all())
        if form.is_valid():

            cleaned_data = form.cleaned_data

            order = Order(name=cleaned_data["name"], jobsite=cleaned_data["jobsite"], date_needed=cleaned_data["date_needed"])
            order.save()

            # delete these from the order -- no longer needed once an order object is created 
            del cleaned_data["name"]
            del cleaned_data["jobsite"]
            del cleaned_data["date_needed"]

            # ROOM FOR OPTIMIZATION HERE?: filter data to only give list of objects that have a quantity requested with them
            def find_requested(cleaned_data):
                requested = []
                for name, value in cleaned_data.items():
                    if int(value) > 0:
                        requested.append(name)
                return requested

            # CREATE ALL ITEMS AND SAVE THEM TO THE ORDER
            for name in find_requested(cleaned_data):
                if name in [s['name'] for s in Sundry.objects.all().values('name')]:
                    i = Item(order=order, text=name, quantity_requested=cleaned_data[name])
                    i.save()
                    # REMOVE FROM QUANTITY AVAILABLE IN SUNDRY MODEL
                    Sundry.objects.filter(name=i.text).update(quantity_available = F('quantity_available') - i.quantity_requested)
                else:
                    i = Item(order=order, text=name, quantity_requested=cleaned_data[name])
                    i.save()
                    # TODO: ASK IF THEY WANT TO MANAGE QUANTITY OF EQUIPMENT 

            
            # HANDLE EMAILING HERE
            subject = 'QCE Warehouse - Order #' + str(order.pk)
            message = 'For: ' + order.name + "\n" + "Jobsite: " + order.jobsite + "\n"
            for item in order.item_set.all():
                message += ("Item Requested: " + item.text + "Quantity: " + str(item.quantity_requested) + "\n")
            message += ("Date Needed: " + str(order.date_needed))
            email_from = settings.EMAIL_HOST_USER
            recipient_list = #HIDDEN FOR PRIVACY

            send_mail(subject, message, email_from, recipient_list)

            # SEND USER TO THANK YOU PAGE -- TODO: redirect to home after a few seconds
            return HttpResponseRedirect('thanks')

    else: 
        form = CreateNewOrder(initial={"name": response.user.username}, sundries = Sundry.objects.all(), equipment = Equipment.objects.all())

    return render(response, "main/order.html", {"sundryList": Sundry.objects.all, "form":form} )

def orderThanks(response):
    return render(response, "main/orderThanks.html", {})

def jobs(response):
    return HttpResponse("<h1>Jobsite 1: Sequim</h1>")
