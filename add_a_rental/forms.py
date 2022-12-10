from .models import rental
from django import forms

class Form(forms.ModelForm):
    class Meta:
        model = rental
        fields = ("__all__")
