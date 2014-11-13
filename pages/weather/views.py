from django.shortcuts import render
from suds.client import Client
from django.http import HttpResponse


def home(request,parm=""):
   url = 'http://www.webservicex.net/globalweather.asmx?WSDL'
   client = Client(url)
   weather =  client.service.GetWeather(parm, 'United States')
   #weather =  client.service.GetCitiesByCountry('United States')

   return HttpResponse(weather)
