from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def dinespotapp(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
def restaurant(request):
    template = loader.get_template('restaurant.html')
    return HttpResponse(template.render())
def reservations(request):
    template = loader.get_template('reservations.html')
    return HttpResponse(template.render())
def business(request):
    template = loader.get_template('business.html')
    return HttpResponse(template.render())