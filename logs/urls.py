from django.urls import path
from logs.helpers.sound import read_sound
from logs.helpers.tmp_hum_sensor import get_tmp_hum

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

read_sound()
get_tmp_hum()