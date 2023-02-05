from django.forms import ModelForm, DateTimeInput
from django.utils import timezone
from .models import Event, Guests


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = (
            "name",
            "event_date",
            "rsvp_by_date",
        )
        widgets ={
            'event_date': DateTimeInput(attrs={'type':'datetime-local', 'min':timezone.now().strftime("%Y-%m-%dT%H:%M")}),
            'rsvp_by_date': DateTimeInput(attrs={'type':'datetime-local', 'min':timezone.now().strftime("%Y-%m-%dT%H:%M")})
        }

class GuestsForm(ModelForm):
    class Meta:
        model = Guests
        fields = (
            "name",
            "party_of",
        )
