from django.urls import path
from . import views

urlpatterns = [
    path('', views.dinespotapp, name='dinespotapp'),
    path('restaurant', views.restaurant, name='restaurant'),
    path('reservations', views.reservations, name='reservations'),
    path('business', views.business, name='business'),
    path('signupClient', views.signupClient, name='signupClient'),
    path('signupRestaurant', views.signupRestaurant, name='signupRestaurant'),
    path('signinClient', views.signinClient, name='signinClient'),
    path('signinRestaurant', views.signinRestaurant, name='signinRestaurant'),
    path('logoutClient', views.logoutClient, name='logoutClient'),
    path('logoutRestaurant', views.logoutRestaurant, name='logoutRestaurant'),
    path('settingsClient', views.settingsClient, name='settingsClient'),
    path('settingsRestaurant', views.settingsRestaurant, name='settingsRestaurant'),
]