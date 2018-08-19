from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('airports', views.AirportView)
router.register('flights', views.FlightView)
router.register('passengers', views.PassengerView)


urlpatterns = [
    path('', views.index, name="index"),
    path('airports/', views.airports, name="airports"),
    path('airports/add', views.add_airport, name="add_airport"),
    path('flights/', views.flights, name="flights"),
    path('flights/<int:flight_id>', views.flight, name="flight"),
    path('passengers/', views.passengers, name="passengers"),
    path('passengers/<int:passenger_id>', views.passenger, name="passenger"),
    path('passengers/<int:passenger_id>/book', views.book, name="book"),
    path('api/', include(router.urls)),
]
