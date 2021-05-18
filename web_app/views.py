from django.shortcuts import render
from api.models import *

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

def enter_reading(request):
  return render(request, 'web_app/add_reading.html')

def about(request):
  return render(request, 'web_app/about.html')