# Generated by Django 5.0.4 on 2024-04-21 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0007_busydate_alter_booking_period_end_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='period_start',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='busydate',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]
