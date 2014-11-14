from django import template
import random

register = template.Library()

@register.inclusion_tag('event_tag.html')
def event_tag(r,c):
      a = {}
      a["location"]="RALEIGH-DURHAM INTERNATIONAL  AIRPORT, NC, United States (KRDU) 35-54N 078-46W 130M"
      a["wind"]= "Variable at 5 MPH (4 KT):0"
      a["wind"]=a["wind"][:a["wind"].find("(")-1]
      a["sky_conditions"]="overcast"
      a["temperature"]="35.1 F (1.7 C)"
      a["temperature"]=a["temperature"][:a["temperature"].find("(")-1]
      a["dewpoint"]="26.1 F (-3.3 C)"
      a["dewpoint"]=a["dewpoint"][:a["dewpoint"].find("(")-1]
      a["rh"]="52%"
      a["pressure"]="30.2 in. Hg (1022 hPa)"
      a["pressure"]=a["pressure"][:a["pressure"].find("(")-1]
      a["status"]="Success"
      if random.random() < 0.5:
         a["rando"]=1
      else:
         a["rando"]=0
      return a
