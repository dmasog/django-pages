from django import template
from weather.models import Reading
import datetime
import random

register = template.Library()

def lookup(dt,h):
   start_date = dt 
   a,b,c = map(int,dt.split("-"))
   print "a",a,"b",b,"c",c
   start_date=datetime.date(a,b,c)+datetime.timedelta(hours=int(h))
   end_date=(start_date+datetime.timedelta(hours=1))#.strftime("%Y-%m-%d"))
   print "ST: ",start_date
   print "ED: ",end_date 
   rec = Reading.objects.filter(dt__range=(start_date, end_date))

   if rec:
      return rec[0].temperature
   return ""
   

@register.simple_tag(takes_context=True)
def date_tag(context,r,c,orig):
      out = context["date"]
      out = out[out.find("/")+1:]
      out = out[:out.find("/")]
      print "R:",r
      if int(c) > orig:
         out = int(out) - 1
      return lookup(r,c)
