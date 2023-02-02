from django.forms import ModelForm
from .models import Event, Guests


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = (
            "name",
            "event_date",
            "rsvp_by_date",
        )

class GuestsForm(ModelForm):
    class Meta:
        model = Guests
        fields = (
            "name",
            "party_of",
        )
