from django.urls import path
from . import views

urlpatterns = [
    path('', views.dinespotapp, name='dinespotapp'),
    path('restaurant/', views.restaurant, name='restaurant'),
    path('reservations/', views.reservations, name='reservations'),
    path('business/', views.business, name='business')
]