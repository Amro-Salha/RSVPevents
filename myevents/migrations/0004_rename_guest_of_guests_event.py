# Generated by Django 4.1.5 on 2023-02-01 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myevents", "0003_guests"),
    ]

    operations = [
        migrations.RenameField(
            model_name="guests",
            old_name="guest_of",
            new_name="event",
        ),
    ]