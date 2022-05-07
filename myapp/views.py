from django.shortcuts import render
from .models import *
from django.contrib import messages
from twilio.rest import Client

# Create your views here.

def index(request):
    return render(request,'index.html')

# def whatsappdata(phone):
#     import time
#     import webbrowser as web
#     import pyautogui as pg
#     phone = "+91"+phone
#     web.open('https://web.whatsapp.com/send?phone='+phone+'&text='+"Thank You")
#     time.sleep(30)
#     pg.press('enter')

def insertcontactdata(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        pincode = request.POST.get('pincode')
        city = request.POST.get('city')
        investment = request.POST.get('investment')

        account_sid = 'ACa28c1bab9b1e9a20d266a481c2708ffb'
        auth_token = '6af73766c7f60977ecb22d5e2ca7ab57'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body="Thak You.",
            from_='+19704802305',
            to=f'+91{phone}'
        )

        print(message.sid)

        # whatsappdata(phone)


        query = contact(name=name, email=email, phone=phone, pincode=pincode, city=city, investment=investment)
        query.save()
        messages.add_message(request, messages.SUCCESS, "data has been submitted")
    else:
        messages.add_message(request, messages.WARNING, "error occured")

    return render(request, 'index.html')
