from django.forms import ModelForm
from api.models import *

class ReadingForm(ModelForm):
  class Meta:
    model = Reading
    fields = ['diastol', 'systol', 'weight']
