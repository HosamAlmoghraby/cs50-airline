from django.shortcuts import render
from django.http import Http404
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


def flight(request, flight_id):
    try:
        flight = Flight.objects.get(pk=flight_id)
    except Flight.DoesNotExist:
        raise Http404("Flight does not exist")
    context = {
        "flight": flight
    }
    return render(request, 'flights/flight.html', context)
