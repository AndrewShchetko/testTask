from django import forms
from .models import *


class FindMenuForm(forms.Form):
    name = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class': 'form-input'}))
