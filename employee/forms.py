from .models import employee
from django import forms
  
# import GeeksModel from models.py
from .models import meeting
  
# create a ModelForm
class Scheduler(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = meeting
        fields = 'title','start_time','end_time','participants','email_id_of_participants','link',
