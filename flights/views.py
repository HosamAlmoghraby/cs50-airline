from django.shortcuts import render
from django.http import Http404
from .models import Airport, Flight, Passenger


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


def passengers(request):
    context = {
        "passengers": Passenger.objects.all()
    }
    return render(request, 'flights/passengers.html', context)


def passenger(request, passenger_id):
    try:
        passenger = Passenger.objects.get(pk=passenger_id)
    except Flight.DoesNotExist:
        raise Http404("Passenger does not exist")
    context = {
        "passenger": passenger
    }
    return render(request, 'flights/passenger.html', context)
