from django.db import models

# Create your models here.
class rental:
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    city = models.CharField( max_length=75)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    picture = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
