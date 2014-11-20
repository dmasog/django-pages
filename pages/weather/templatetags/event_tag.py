from django import template
from weather.models import Reading
import datetime
from pytz import timezone
import random

register = template.Library()

def lookup(dt,h,orig,slug):
   if h == 18:
      print "Lookup:",dt,h,orig,slug
   start_date = dt
   a,b,c = map(int,dt.split("-"))
   h = int(h)
   eastern = timezone('US/Eastern')
   #eastern = timezone("UTC")
   start_date=datetime.datetime(a,b,c,h,tzinfo=eastern)
   end_date=datetime.datetime(a,b,c,h,tzinfo=eastern)+datetime.timedelta(hours=1)
   rec = Reading.objects.filter(dt__range=(start_date, end_date),slug=slug)

   if len(rec)>0:
      return rec[0],len(rec)
   return "",0

@register.inclusion_tag('event_tag.html')
def event_tag(r,c,orig,slug):
      l,llen = "",""
      
      if int(c)<=int(orig): 
          l,llen = lookup(r,c,orig,slug)
      else:
          a1,b1,c1 = map(int,r.split("-"))
          d = datetime.date(a1,b1,c1)
          r = d - datetime.timedelta(days=1)
          r = r.strftime("%Y-%m-%d")

          l,llen = lookup(r,c,orig,slug)
      a = {}
      if llen > 0:
         a["location"]=l.location
         a["wind"]= l.wind
         a["wind"]=a["wind"][:a["wind"].find("(")-1]
         a["sky_conditions"]=l.sky_conditions
         a["temperature"]=l.temperature
         a["temperature"]=a["temperature"][:a["temperature"].find("(")-1]
         a["dewpoint"]=l.dewpoint
         a["dewpoint"]=a["dewpoint"][:a["dewpoint"].find("(")-1]
         a["rh"]=l.rh+" RH"
         a["pressure"]=l.pressure
         a["pressure"]=a["pressure"][:a["pressure"].find("(")-1]
         a["status"]=l.status
         a["rando"]=1
      else:
         a["rando"]=0
      return a
