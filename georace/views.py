from django.shortcuts import render
from georace.models import Event
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def index(request):
    return render(request, 'index.html', {
        'active': 'home'
    })

def events(request):
    events = Event.objects.all()
    return render(request, 'events.html', {
        'events': events,
        'active': 'events'
    })

def contacts(request):
    return render(request, 'contacts.html', {
        'active': 'contacts'
    })

def donate(request):
    return render(request, 'donate.html', {
        'active': 'donate'
    })

def register(request):
    if request.method =='POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request,
                'index.html', {
                'active': 'home'
            })
    else:
        form = UserCreationForm() # An unbound form

    return render(request, 'registration/register.html', {'form': form})
