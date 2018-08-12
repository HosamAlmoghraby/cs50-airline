from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('airports/', views.airports),
    path('flights/', views.flights),
]
