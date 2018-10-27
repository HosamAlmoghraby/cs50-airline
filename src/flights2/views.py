from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .models import Airport, Flight, Passenger
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'flights2/index.html')


def airports(request):
    airports = Airport.objects.all()

    context = {
        "airports": airports
    }
    return render(request, 'flights2/airports.html', context)


def flights(request):
    flights = Flight.objects.all()
    
    context = {
        "flights": flights
    }
    return render(request, 'flights2/flights.html', context)


def flight(request, flight_id):
    try:
        flight = Flight.objects.get(pk=flight_id)
    except Flight.DoesNotExist:
        raise Http404("Flight does not exist")
    
    passengers = flight.passengers.all()

    context = {
        "flight": flight,
        "passengers": passengers
    }
    return render(request, 'flights2/flight.html', context)


def passengers(request):
    passengers = Passenger.objects.all()

    context = {
        "passengers": passengers
    }
    return render(request, 'flights2/passengers.html', context)


def passenger(request, passenger_id):
    try:
        passenger = Passenger.objects.get(pk=passenger_id)
    except Passenger.DoesNotExist:
        raise Http404("Passenger does not exist")

    flights = passenger.flights.all()
    non_flights = Flight.objects.exclude(passengers=passenger)

    context = {
        "passenger": passenger,
        "flights": flights,
        "non_flights": non_flights
    }
    return render(request, 'flights2/passenger.html', context)


def book(request, passenger_id):
    try:
        flight_id = int(request.POST["flight"])
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=passenger_id)
    except KeyError:
        return render(request, "flights2/error.html", {"message": "No Selection!"})
    except Flight.DoesNotExist:
        return render(request, "flights2/error.html", {"message": "No Flight!"})
    except Passenger.DoesNotExist:
        return render(request, "flights2/error.html", {"message": "No Passenger!"})

    passenger.flights.add(flight)
    return HttpResponseRedirect(reverse('flights2:passenger', args=(passenger_id,)))


def add_airport(request):
    if request.method == 'POST':
        Airport.objects.create(
            code = request.POST["code"],
            city = request.POST["city"]
            )
        # airport = Airport()
        # airport.code = request.POST["code"]
        # airport.city = request.POST["city"]
        # airport.save()
        return HttpResponseRedirect(reverse("flights2:airports"))
    else:
        return render(request, 'flights2/add_airport.html')
