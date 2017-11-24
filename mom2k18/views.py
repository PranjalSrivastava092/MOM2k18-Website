from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Info , Register
from django.views.generic.edit import CreateView


def home(request):
    return render(request, 'home.html',{'title': 'home | MOM2k18'})

def about(request):
    return render(request, 'About.html',{'title': 'about | MOM2k18'})

def events(request):
    return render(request, 'events.html',{'title': 'events | MOM2k18'})

def mad(request):
    return render(request, 'MAD1.html',{'title': 'MAD | MOM2k18'})

def brainwave(request):
    return render(request, 'brainwave1.html',{'title': 'brainwave | MOM2k18'})

def hospi(request):
    return render(request, 'Hospitality.html',{'title': 'hospitality | MOM2k18'})

def quiz(request):
    return render(request, 'quiz1.html',{'title': 'quiz | MOM2k18'})

def sponsors(request):
    return render(request, 'Sponsors.html',{'title': 'sponsors | MOM2k18'})

def team(request):
    return render(request, 'Team.html',{'title': 'team | MOM2k18'})

def tme(request):
    return render(request, 'TME1.html',{'title': 'tme | MOM2k18'})

def one(request):
    return render(request, 'home.html',{'title': 'one | MOM2k18'})

def message(request):
    return render(request, 'message.html',{'title': 'message | MOM2k18'})

def gallery(request):
    return render(request, 'gallery.html',{'title':'gallery | MOM2k18'})

def cultural(request):
    return render(request, 'cultural.html',{'title':'cultural | MOM2k18'})

def rangmanch(request):
    return render(request, 'rangmanch1.html',{'title': 'rangmanch | MOM2k18'})

def bandwars(request):
    return render(request, 'bandwars1.html',{'title': 'bandwars | MOM2k18'})

class register(CreateView):
    model = Register

    fields = ['name', 'email', 'city', 'address', 'phone_number', 'institute', 'event', 'message']






