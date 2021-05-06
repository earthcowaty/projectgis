from django.db import models

# Create your models here.
class fourCModel(models.Model):
    Country=models.CharField(max_length=1000)
    Pm25=models.FloatField(max_length=1000)
    Year=models.IntegerField()
