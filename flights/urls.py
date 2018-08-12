from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('airports/', views.airports),
    path('flights/', views.flights),
    path('flights/<int:flight_id>', views.flight),
]
