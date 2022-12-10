from django.db import models
import datetime
import uuid

# Create your models here.
class Booking(models.Model):

    ID_rental = models.CharField(max_length=50)
    ID_booking = models.CharField(primary_key=True, default=uuid.uuid4().hex[:5].upper(), max_length=50, editable=False)
    ID_guest = models.CharField(max_length=50)
    tanggal_checkin = models.DateField(blank=True, null=True, default=datetime.date.today)
    tanggal_checkout = models.DateField(blank=True, null=True, default=datetime.date.today)
    harga = models.IntegerField(max_length=20)

    def __str__(self):
        return str(self.ID_booking)