# Generated by Django 5.0.4 on 2024-04-16 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_alter_booking_car_alter_booking_period_end_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UnavailableDate',
        ),
    ]
