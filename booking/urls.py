from django.urls import path
from .views import *

app_name = "booking"

urlpatterns = [
    path('', index, name='index'),
    path('form', add_booking, name='form'),
]