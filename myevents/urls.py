from django.urls import path
from .views import home, user_home, my_events, create_event, invite, event_details, guest_list

urlpatterns = [
    path("", home, name="home"),
    path("user_home/", user_home, name="user_home"),
    path("my_events/", my_events, name="my_events"),
    path("create_event/", create_event, name="create_event"),
    path("event/<int:id>/invite/", invite, name='invite'),
    path("<int:id>/", event_details, name='event_details'),
    path('event/<int:id>/', guest_list, name='guest_list'),
]
