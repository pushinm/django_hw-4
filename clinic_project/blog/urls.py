from django.urls import path
from .views import about, contact, home

urlpatterns = [
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('home', home, name='home')
]
