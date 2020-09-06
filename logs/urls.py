from django.urls import path
from logs.helpers.sound import read_sound

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

read_sound()