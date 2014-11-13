from django.shortcuts import render
from suds.client import Client
from django.http import HttpResponse


def home(request):
   url = 'http://www.webservicex.net/globalweather.asmx?WSDL'
   client = Client(url)
   #print client
   weather =  client.service.GetWeather('Bemidji', 'United States')
   #weather =  client.service.GetCitiesByCountry('United States')
   print weather

   return HttpResponse(weather)
