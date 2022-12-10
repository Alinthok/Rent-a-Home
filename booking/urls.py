from django.urls import path
from .views import *

app_name = "booking"

urlpatterns = [
    path('', index, name='index'),
    path('get', get_booking, name='get'),
    path('create', create_booking, name='create'),
    path('delete/<str:ID_booking>', delete_booking, name='delete'),
]