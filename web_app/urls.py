from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('register', views.register, name = 'register'),
    path('login', views.login, name = 'login'),
    path('readings/<str:pk>', views.readings, name = 'readings'),
    path('clinician_view/<str:pk>', views.clinician_view, name = 'clinician_view'),
    path('add', views.enter_reading, name = 'add'),
    path('about', views.about, name = 'about'),
]