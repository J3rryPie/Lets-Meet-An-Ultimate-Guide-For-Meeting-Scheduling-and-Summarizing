from .models import employee
from django import forms
class AForm(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(widget = forms.PasswordInput())
