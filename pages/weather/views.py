from django.shortcuts import render
from suds.client import Client
from django.http import HttpResponse
from django.template import Context, Template
from weather.models import Reading
import os
import datetime
import xml.etree.ElementTree as ET

# Create your views here.
ctext = {}
ctext["Carrier"]="USPS"
ctext["Weather_Title"]="Weather History"
ctext["Weather_Tagline"]="Weather readings for the last 3 days"
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

def home(request,parm=""):
   ctext["dates"]=[]
   if "date" in request.REQUEST:
       for i in range(3):
           a,b,c = request.REQUEST["date"].split("/")
           ctext["dates"].append((datetime.date(int(c),int(b),int(a))-datetime.timedelta(i)).strftime("%m/%d/%y"))
   else:
       for i in range(3):
           ctext["dates"].append((datetime.datetime.today()-datetime.timedelta(i)).strftime("%m/%d/%y"))

   url = 'http://www.webservicex.net/globalweather.asmx?WSDL'
   client = Client(url)
   #parm = parm.replace(chr(20)," ")
   weather =  client.service.GetWeather(parm, 'United States')
   f = open(parm,"w")
   weather = weather.replace('encoding="utf-16"','')
   f.write(weather)
   f.close()
   f = None
   doc = ET.parse(parm)
   root = doc.getroot()
   fds = []   
   for el in root:
      if el.tag in ["Location","Wind","SkyConditions","Temperature","DewPoint","RelativeHumidity","Pressure","Status"]:
          fds.append(el.text)
   print "FDS:",len(fds),fds
   r = Reading(location=fds[0],wind=fds[1],sky_conditions=fds[2],temperature=fds[3],dewpoint=fds[4],rh=fds[5],pressure=fds[6],status=fds[7])
   r.save()
   os.remove(parm)

   #weather =  client.service.GetCitiesByCountry('United States')

   #return HttpResponse(weather)
   return render(request,"weather.html",Context(ctext))
