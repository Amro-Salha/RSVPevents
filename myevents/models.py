from django.db import models
from django.conf import settings

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=150)
    event_date = models.DateTimeField()
    rsvp_by_date = models.DateTimeField()

    host = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        related_name="events",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

    def total_guests(self):
        total = 0
        for guest in self.guests.all():
            total += guest.party_of
        return total


class Guests(models.Model):
    name = models.CharField(max_length=150)
    party_of = models.IntegerField()

    event = models.ForeignKey(
        Event,
        related_name="guests",
        on_delete=models.CASCADE,
    )
