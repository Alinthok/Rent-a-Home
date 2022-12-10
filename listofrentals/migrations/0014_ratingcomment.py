# Generated by Django 4.0.4 on 2022-12-09 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_initial'),
        ('listofrentals', '0013_rating_unique_user_per_rental'),
    ]

    operations = [
        migrations.CreateModel(
            name='RatingComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('rating', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='listofrentals.rating')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='homepage.generaluser')),
            ],
        ),
    ]