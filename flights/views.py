from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .models import Airport, Flight, Passenger
from django.urls import reverse
from rest_framework import viewsets
from .serializers import AirportSerializer


class AirportView(viewsets.ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer


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
        "flight": flight,
        "passengers": flight.passengers.all()
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
    except Passenger.DoesNotExist:
        raise Http404("Passenger does not exist")
    context = {
        "passenger": passenger,
        "flights": passenger.flights.all(),
        "non_flights": Flight.objects.exclude(passengers=passenger)
    }
    return render(request, 'flights/passenger.html', context)


def book(request, passenger_id):
    try:
        flight_id = int(request.POST["flight"])
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=passenger_id)
    except KeyError:
        return render(request, "flights/error.html", {"message": "No Selection!"})
    except Flight.DoesNotExist:
        return render(request, "flights/error.html", {"message": "No Flight!"})
    except Passenger.DoesNotExist:
        return render(request, "flights/error.html", {"message": "No Passenger!"})

    passenger.flights.add(flight)
    return HttpResponseRedirect(reverse('passenger', args=(passenger_id,)))
