from django.shortcuts import render
from api.models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'web_app/index.html')

def register(request):
    return render(request, 'web_app/register.html')

def login(request):
    return render(request, 'web_app/login.html')

def readings(request, pk):
  readings = Reading.objects.filter(patient = pk)
  return render(request, 'web_app/readings.html', {'readings': readings})

def clinician_view(request, pk):
  patients = Patient.objects.filter(doctor = pk)
  return render(request, 'web_app/clinician_view.html', {'patients': patients})

def enter_reading(request):
  form = ReadingForm()
  context = {'form': form}
  return render(request, 'web_app/add_reading.html', context)

def about(request):
  return render(request, 'web_app/about.html')
