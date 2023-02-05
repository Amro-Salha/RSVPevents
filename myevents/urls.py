from django.urls import path
from .views import home, user_home, my_events, create_event, invite, event_details, guest_list, edit_event, delete_event, access_denied

urlpatterns = [
    path("", home, name="home"),
    path("user_home/", user_home, name="user_home"),
    path("my_events/", my_events, name="my_events"),
    path("create_event/", create_event, name="create_event"),
    path("event/<int:id>/invite/", invite, name='invite'),
    path("<int:id>/", event_details, name='event_details'),
    path('event/guest_list/<int:id>/', guest_list, name='guest_list'),
    path('event/edit/<int:id>/', edit_event, name='edit'),
    path('event/delete/<int:id>/', delete_event, name='delete'),
    path("access_denied/", access_denied, name="access_denied"),
]
