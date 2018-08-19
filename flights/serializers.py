from rest_framework import serializers
from .models import Airport, Flight, Passenger


class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = ('code', 'city')


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ('__all__')


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = ('__all__')
