# Generated by Django 3.2 on 2023-08-09 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_appointment_photographer_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_total_price',
            field=models.FloatField(),
        ),
    ]
