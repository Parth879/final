from django.shortcuts import render
from .models import *
from django.contrib import messages
import requests
# Create your views here.
MESSAGE_TAGS = {
    messages.SUCCESS: 'success',
    messages.WARNING: 'danger'
}

def index(request):
    return render(request,'index.html')



def insertcontactdata(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        pincode = request.POST.get('pincode')
        city = request.POST.get('city')
        investment = request.POST.get('investment')

        url = f"https://onlysms.co.in/api/sms.aspx?UserID=DHAMENTDND&UserPass=Dhm@369&MobileNo={phone}&GSMID=KBKADV&PEID=1701162244536230346&Message=Dear Client Trade summary Relience 100 share buy @235.223 SBI Sale 100 share @358.56  total out standing Rs. 435 KBKADV&TEMPID=1707162503246916721&UNICODE=TEXT"
        response= requests.get(url)
        response.text

        query = contact(name=name, email=email, phone=phone, pincode=pincode, city=city, investment=investment)
        query.save()
        messages.add_message(request, messages.SUCCESS, "data has been submitted")
    else:
        messages.error(request, "error occured")

    return render(request, 'index.html')
