from django import template

register = template.Library()

@register.inclusion_tag('event_tag.html')
def event_tag(r,c):
      a = {}
      a["temperature"]=87
      return a
