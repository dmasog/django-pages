from django.shortcuts import render
from suds.client import Client
from django.http import HttpResponse
from django.template import Context, Template
from django.utils.text import slugify
from weather.models import Reading
import os
import datetime
import time
import xml.etree.ElementTree as ET

os.environ['TZ'] = "EST"
time.tzset()
# Create your views here.
ctext = {}
ctext["Page_Title"]="Weather History"
ctext["Carrier"]="USPS"
ctext["Weather_Title"]="Weather History"
ctext["Weather_Tagline"]="Weather readings for "
ctext["Address"]="7321 Sweet Bay LN<br>Raleigh NC 27615"
ctext["Order_Number"]="05-00032"
ctext["TrackingNo"]="LN430450976CN"
ctext["Company_Address"]="7321 Sweet Bay LN<br>Raleigh NC 27615"
ctext["Company_Email"]="dave@masog.com"
ctext["Company_Phone"]="919 289 9253"
ctext["Checkpoints_Completed"]=3
ctext["Checkpoints"]=["First","Second","Third","Fourth","Fifth"]
ctext["Chkpts"]=[1,2,3,4,5]
ctext["ShippingPoints_Location"]=["January 23, 2014, 11:03 am, Alexandria VA US","January 24, 2014, 10:12 am, Alexandria VA US","January 25, 2014, 03:20 pm, Alexandria VA US","January 26, 2014, 05:15 pm, Alexandria VA US","January 27, 2014, 09:10 am, Alexandria VA US","January 28, 2014, 11:03 am, Alexandria VA US","January 29, 2014, 10:12 am, Alexandria VA US","January 30, 2014, 05:15 pm, Alexandria VA US"]
ctext["ShippingPoints_Status"]=["Shipped","Out for delivery","Package arrived at a carrier facility","Package arrived at a carrier facility","Package arrived at a carrier facility","Package arrived at a carrier facility","Package arrived at a carrier facility","Package arrived at a carrier facility"]

def lookup(dt,slug):
   rec = Reading.objects.filter(d=dt,slug=slug)
   print rec
   
def home(request,parm=""):
   ctext["dates"]=[]
   for i in range(4):
       if "date" in request.REQUEST:
           a,b,c = map(int,request.REQUEST["date"].split("-"))
           ctext["dates"].append((datetime.date(c,a,b)-datetime.timedelta(i)).strftime("%Y-%m-%d"))
       else:
           ctext["dates"].append((datetime.datetime.today()-datetime.timedelta(i)).strftime("%Y-%m-%d"))
   ctext["slug"]=slugify(parm)
   try:
       client = Client('http://www.webservicex.net/globalweather.asmx?WSDL',timeout=5)
       weather =  client.service.GetWeather(parm, 'United States')
       with open(parm,"w") as f:
          weather = weather.replace('encoding="utf-16"','')
          f.write(weather)

       root = ET.parse(parm).getroot()
       fds = []   
       for el in root:
           if el.tag in ["Location","Wind","SkyConditions","Temperature","DewPoint","RelativeHumidity","Pressure","Status"]:
               if el.text.find("Windchill")<0:
                  fds.append(el.text)
       os.remove(parm)
       r = Reading(slug=slugify(parm),location=fds[0],wind=fds[1],sky_conditions=fds[2],temperature=fds[3],dewpoint=fds[4],rh=fds[5],pressure=fds[6],status=fds[7])
       r.save()
   except:
       print "Webservice Error" #Database Exception
   finally:
       pass
   #weather =  client.service.GetCitiesByCountry('United States')

   return render(request,"weather.html",Context(ctext))
