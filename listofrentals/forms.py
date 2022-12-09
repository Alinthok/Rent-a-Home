from django import forms
from .models import Rating, RatingComment

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = {'rating', 'comment'}

        widgets = {
            'comment' : forms.Textarea(attrs={'class': 'form-control'}),
        }

class RatingCommentForm(forms.ModelForm):
    class Meta:
        model = RatingComment
        fields = {'comment', 'user', 'rating'}
        exclude = ('user', 'rating')
        widgets = {
            'comment' : forms.Textarea(attrs={'class': 'form-control'}),
        }