from .models import add_rental
from django import forms

class Form(forms.Form):
    class Meta:
        model = add_rental
        fields = ("__all__")
