from listofrentals.models import Rental
from django import forms

class Form(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ("__all__")
