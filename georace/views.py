from django.shortcuts import render
from georace.models import Event
# Create your views here.

def index(request):
    events = Event.objects.all()
    return render(request, 'index.html', {
        'events': events,
        'active': 'home'
    })

def events(request):
    events = Event.objects.all()
    return render(request, 'index.html', {
        'events': events,
        'active': 'events'
    })

def about(request):
    events = Event.objects.all()
    return render(request, 'index.html', {
        'events': events,
        'active': 'about'
    })

def donate(request):
    events = Event.objects.all()
    return render(request, 'index.html', {
        'events': events,
        'active': 'donate'
    })
