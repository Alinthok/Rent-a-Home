# Generated by Django 4.0.4 on 2022-12-09 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listofrentals', '0007_remove_rating_comment_ratingcomment_ratig'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ratingcomment',
            old_name='ratig',
            new_name='rating',
        ),
    ]
