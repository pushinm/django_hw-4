from django.shortcuts import render
from django.http import HttpResponse
from .models import Clinic
# Create your views here.
def about(request):
    template_ = 'about.html'

    doctors = Clinic.objects.all()

    context = {
        'doctors': doctors
    }

    return render(request, template_name=template_, context=context)\


def contact(request):
    template_ = 'contact.html'

    doctors = Clinic.objects.all()

    context = {
        'doctors': doctors
    }

    return render(request, template_name=template_, context=context)

def home(request):
    template_ = 'home.html'

    context={}

    return render(request, template_name=template_, context=context)