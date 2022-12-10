from django import forms
from .models import GeneralUser

class GeneralUserForm(forms.ModelForm):

    class Meta:
        model = GeneralUser
        exclude = ('user', )