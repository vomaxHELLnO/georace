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
    return render(request, 'events.html', {
        'events': events,
        'active': 'events'
    })

def contacts(request):
    events = Event.objects.all()
    return render(request, 'contacts.html', {
        'events': events,
        'active': 'contacts'
    })

def donate(request):
    events = Event.objects.all()
    return render(request, 'donate.html', {
        'events': events,
        'active': 'donate'
    })
