from django.contrib import admin
from .models import Event, Guests

# Register your models here.

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("name", "event_date", "rsvp_by_date", "id")

@admin.register(Guests)
class GuestsAdmin(admin.ModelAdmin):
    list_display = ("name", "party_of", "event", "id")
