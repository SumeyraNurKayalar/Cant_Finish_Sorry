from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.

def index(request):
    return render(request, "template_app/first.html")

def weather_view(request):
    weather_dictionary = {"Adana" : "45", "Edirne" : "30"}
    return render(request, "template_app/weather.html", context=weather_dictionary)