from django import template
from weather.models import Reading
import datetime
import random
from pytz import timezone

register = template.Library()

def lookup(dt,h,slug):
   start_date = dt 
   a,b,c = map(int,dt.split("-"))
   h = int(h)
   eastern = timezone('US/Eastern')
   #eastern = timezone("UTC")
   start_date=datetime.datetime(a,b,c,h,tzinfo=eastern)
   end_date=datetime.datetime(a,b,c,h,tzinfo=eastern)+datetime.timedelta(hours=1)
   rec = Reading.objects.filter(dt__range=(start_date, end_date),slug=slug)

   if len(rec)>0:
      return rec[0].temperature,len(rec)
   return ""
   

@register.simple_tag(takes_context=True)
def date_tag(context,r,c,orig,slug):
      out = context["date"]
      out = out[out.find("/")+1:]
      out = out[:out.find("/")]
      if int(c) > orig:
         out = int(out) - 1
      #return str(r) + " " + str(c)
      return lookup(r,c,slug)
