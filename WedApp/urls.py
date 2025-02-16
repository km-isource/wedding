from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('messages/', views.messages, name='messages'),
    path('add-messages/', views.add_message, name='add_messages'),
    path('submit-rsvp/', views.submit_rsvp, name='submit_rsvp')
]