from django import forms
from django.forms import ModelForm
from .models import Booking
from django.forms.widgets import Input, Select, DateInput

class BookingForm(ModelForm):
    class Meta :
        model = Booking
        fields = ['ID_rental', 'ID_guest', 'tanggal_checkin', 'tanggal_checkout']
        widgets = {
            # Contoh nanti nambahin atribut buat styling css : 'judul' : forms.TextInput(attrs={"class": "form-control"}),
            'ID_rental' : forms.TextInput(attrs={"class": "form-control"}),
            'ID_guest' : forms.TextInput(attrs={"class": "form-control"}),
            'tanggal_checkin' : forms.DateInput(attrs={'type':'date', "class": "form-control"}),
            'tanggal_checkout' : forms.DateInput(attrs={'type':'date', "class": "form-control"}),
        }