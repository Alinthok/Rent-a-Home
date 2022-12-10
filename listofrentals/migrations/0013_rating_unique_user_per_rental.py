# Generated by Django 4.0.4 on 2022-12-09 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listofrentals', '0012_remove_rental_rating_rating_comment_rating_rental_and_more'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='rating',
            constraint=models.UniqueConstraint(fields=('user', 'rental'), name='unique_user_per_rental'),
        ),
    ]