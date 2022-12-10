import payment
from .models import Payment
from django import forms

class Form(forms.ModelForm):
    class Meta:
        model = payment
        fields = ("__all__")