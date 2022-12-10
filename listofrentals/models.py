from django.db import models
from django.utils.text import slugify
from homepage.models import GeneralUser
from django.db.models import Avg, Count

# Create your models here:
class Rental(models.Model):
    rent_name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.TextField()
    img = models.TextField()
    slug = models.SlugField(max_length=50)

    def calculateAvgRating(self):
        rating = Rating.objects.filter(rental=self).aggregate(avarage=Avg('rating'))
        avg=0
        if rating["avarage"] is not None:
            avg=float(rating["avarage"])
        return avg

    def getRatingsCount(self):
        rating = Rating.objects.filter(rental=self)
        r = []
        for i in range(0, 5):
            r.append(len(rating.filter(rating=i+1)))
        return r

    def __str__(self):
        return self.rent_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.rent_name)
        super(Rental, self).save(*args, **kwargs)

class Rating(models.Model):
    class RatingClass(models.IntegerChoices):
        VERYBAD = 1
        BAD = 2
        NORMAL = 3
        GOOD = 4
        VERYGOOD = 5

    rating = models.IntegerField(choices=RatingClass.choices)
    comment = models.TextField()
    user = models.ForeignKey(GeneralUser, on_delete=models.CASCADE, null=True)
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE, null=True)   

    def getComments(self):
        ratingComments = RatingComment.objects.filter(rating=self)
        return ratingComments

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'rental'], name='unique_user_per_rental'
            )
        ]

class RatingComment(models.Model):
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(GeneralUser, on_delete=models.CASCADE, null=True)
    comment = models.TextField()
