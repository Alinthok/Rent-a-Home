# Generated by Django 4.0.4 on 2022-12-09 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_initial'),
        ('listofrentals', '0011_ratingcomment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rental',
            name='rating',
        ),
        migrations.AddField(
            model_name='rating',
            name='comment',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rating',
            name='rental',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='listofrentals.rental'),
        ),
        migrations.AddField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='homepage.generaluser'),
        ),
        migrations.DeleteModel(
            name='RatingComment',
        ),
    ]
