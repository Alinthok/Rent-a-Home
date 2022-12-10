from django.db import models

# Create your models here.
rental_type = (('apartment', 'APARTMENT'), ('home', 'HOME'))
class rental(models.Model):
    id_rental = models.CharField(max_length=25)
    rental_type = models.CharField(max_length=10,choices=rental_type, default='home')
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    city = models.CharField( max_length=75)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    picture = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    
    def __str__(self):
        return str(self.id_rental)