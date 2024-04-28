from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('terminal', views.terminal, name='terminal'),
    path('tankstorage', views.tankstorage, name='tankstorage'),
    path('contact', views.contact, name='contact'),
]