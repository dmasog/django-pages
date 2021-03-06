from django.db import models
from datetime import datetime

class Reading(models.Model):
    slug = models.SlugField(max_length=40,default="raleigh")
    d  = models.DateField(default=datetime.now())
    dt = models.DateTimeField(default=datetime.now)
    location = models.CharField(max_length=200)
    wind = models.CharField(max_length=75)
    sky_conditions = models.CharField(max_length=30)
    temperature = models.CharField(max_length=30)
    dewpoint = models.CharField(max_length=30)
    rh = models.CharField(max_length=30)
    pressure = models.CharField(max_length=30)
    status = models.CharField(max_length=30)

    def __unicode__(self):
        return self.temperature + " -  " + self.location

