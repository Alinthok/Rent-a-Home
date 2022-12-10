from django.contrib import admin
from .models import Rental, Rating, RatingComment

# Register your models here.
admin.site.register(Rental)
admin.site.register(Rating)
admin.site.register(RatingComment)