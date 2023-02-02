from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Event, Guests
from .forms import EventForm, GuestsForm

# Create your views here.
def home(request):
    return render(request, 'myevents/home.html')

@login_required
def user_home(request):
    return render(request, 'myevents/user_home.html')

@login_required
def my_events(request):
    events = Event.objects.filter(host=request.user)
    total_guests = {}

    for event in events:
        total = 0
        for guest in event.guests.all():
            total += guest.party_of
        total_guests[event.id] = total

    context = {
        "events" : events,
        "total_guests":total_guests,
    }
    return render(request, 'myevents/my_events.html', context)

@login_required
def create_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(False)
            event.host = request.user
            event = form.save()
            return(redirect("my_events"))
    else:
        form = EventForm()
    context = {
        "form" : form,
    }
    return render(request, 'myevents/create_event.html', context)

def invite(request, id):
    event = Event.objects.get(id = id)
    if request.method == "POST":
        form = GuestsForm(request.POST)
        if form.is_valid():
            guest = form.save(False)
            guest.event = event
            guest.save()
            return(redirect("guest_list", event.id))
    else:
        form = GuestsForm()
    context = {
        "form":form,
        "event":event
    }
    return render(request, 'myevents/invite.html', context)

@login_required
def event_details(request, id):
    event = get_object_or_404(Event, id=id)
    guests = Guests.objects.filter(event=event)
    total_guests = event.total_guests

    context = {"event": event, "guests" : guests, "total_guests":total_guests,}
    return render(request, "myevents/event_details.html", context)

def guest_list(request, id):
    event = Event.objects.get(id=id)
    guests = Guests.objects.filter(event=event)
    total_guests = event.total_guests
    context = {
        "event":event,
        "guests": guests,
        "total_guests":total_guests
    }
    return render(request, "myevents/guest_list.html", context)
