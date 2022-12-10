from django.urls import path
from .views import *

app_name = "booking"

urlpatterns = [
    path('', index, name='index'),
    path('form', create_booking, name='form'),
    path('delete/<str:ID_booking>', delete_booking, name='delete'),
]