from django.shortcuts import render
from .models import Airport, Flight


# Create your views here.
def index(request):
    return render(request, 'flights/index.html')


def airports(request):
    context = {
        "airports": Airport.objects.all()
    }
    return render(request, 'flights/airports.html', context)


def flights(request):
    context = {
        "flights": Flight.objects.all()
    }
    return render(request, 'flights/flights.html', context)
