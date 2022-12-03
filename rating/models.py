from django.db import models

# Create your models here.
class Rating(models.Model):
    class RatingClass(models.IntegerChoices):
        VERYBAD = 1
        BAD = 2
        NORMAL = 3
        GOOD = 4
        VERYGOOD = 5

    rating = models.IntegerField(choices=RatingClass.choices)
    # to do : ONE on ONE relationship to GeneralUser Model
    # to do : ONE on ONE relationship to Rentals Model

class RatingComment(models.Model):
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE)
    comment = models.TextField()
    # to do : ONE on ONE relationship to GeneralUser Model