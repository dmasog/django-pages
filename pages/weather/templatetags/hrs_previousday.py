from django import template

register = template.Library()

@register.filter
def hrs_previousday(value):
    if value < 0:
       return int(value) + 24
    elif value > 23:
       print value
       return int(value) - 24
    else:
       return value
