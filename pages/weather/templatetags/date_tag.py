from django import template
import random

register = template.Library()

@register.simple_tag(takes_context=True)
def date_tag(context,r,c,orig):
      out = context["date"]
      out = out[out.find("/")+1:]
      out = out[:out.find("/")]
      print "R:",r
      if int(c) > orig:
         out = int(out) - 1
      return str(out)+" "+str(c)
