from django import forms
from .models import Text

class TextForm(forms.ModelForm):
    transcript=forms.CharField()
    class Meta:
        model=Text
        fields=[
        'transcript'
        ]