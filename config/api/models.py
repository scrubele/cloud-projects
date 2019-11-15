from django.db import models

# Create your models here.

class Sensor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    sensor_type = models.CharField(max_length=250)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    measurement_value = models.FloatField(blank=True, null=True)