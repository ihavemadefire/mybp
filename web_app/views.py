from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'web_app/index.html')

def register(request):
    return render(request, 'web_app/register.html')

def login(request):
    return render(request, 'web_app/login.html')

def readings(request):
  return render(request, 'web_app/readings.html')

def enter_reading(request):
  return render(request, 'web_app/add_reading.html')