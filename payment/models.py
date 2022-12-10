from django.db import models
import datetime
import uuid

# Create your models here.
PAYMENT_CHOICES = (
    ('GP', 'GoPay'),
    ('SP', 'ShopeePay'),
    ('OVO', 'OVO'),
    ('AMIM', 'Alfamart/Indomart')
)

class Payment(models.Model):
    ID_booking = models.CharField(primary_key=True, default=uuid.uuid4().hex[:5].upper(), max_length=50, editable=False)
    harga_booking = models.IntegerField(max_length=20)
    cara_pembayaran = models.CharField(max_lenght=50, choices=PAYMENT_CHOICES)
    

    def __str__(self):
        return str(self.ID_booking)