from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template

# Create your views here.
ctext = {}
def home(request):
    return render(request,"events-schedule.html",Context(ctext))
