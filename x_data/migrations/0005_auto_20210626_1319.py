# Generated by Django 3.1.6 on 2021-06-26 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('x_data', '0004_auto_20210626_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='petaint',
            name='Eye_infection',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='petaint',
            name='Oxigen_leval',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='petaint',
            name='Rendesiver_dose',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='petaint',
            name='Ventilator',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AddField(
            model_name='petaint',
            name='blood_preshar',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]