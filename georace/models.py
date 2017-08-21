from django.db import models
from location_field.models.plain import PlainLocationField
from django.contrib.auth.models import User


class Event(models.Model):
    name = models.CharField(max_length=255)
    place = models.CharField(max_length=255, null=True)
    geotag = PlainLocationField(based_fields=['place'], zoom=7, null=True)
