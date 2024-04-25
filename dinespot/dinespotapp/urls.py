from django.urls import path
from . import views

urlpatterns = [
    path('dinespotapp/', views.dinespotapp, name='dinespotapp'),
]