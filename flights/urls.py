from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Airport', views.AirportView)


urlpatterns = [
    path('', views.index, name="index"),
    path('airports/', views.airports, name="airports"),
    path('flights/', views.flights, name="flights"),
    path('flights/<int:flight_id>', views.flight, name="flight"),
    path('passengers/', views.passengers, name="passengers"),
    path('passengers/<int:passenger_id>', views.passenger, name="passenger"),
    path('passengers/<int:passenger_id>/book', views.book, name="book"),
    path('api/', include(router.urls)),
]
