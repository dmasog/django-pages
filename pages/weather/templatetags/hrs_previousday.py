from django import template

register = template.Library()

@register.filter
def hrs_previousday(value):
    if value < 0:
       return value + 24
    elif value > 23:
       return value - 24
    else:
       return value
