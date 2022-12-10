from django.db import models
from django.contrib.auth.models import User

class GeneralUser(models.Model):
    ROLES = [
        ('G', 'Guest'),
        ('L', 'Landlord'),
        ('A', 'Admin'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=1, choices=ROLES)

    def __str__(self):
        return self.user.username