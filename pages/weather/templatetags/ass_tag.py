from django import template
import random

register = template.Library()

@register.assignment_tag
def ass_tag(d,format_string):
      import datetime
      val =  datetime.datetime.now().strftime(format_string).lstrip("0")
      if val == "":
         val = 0
      return val
