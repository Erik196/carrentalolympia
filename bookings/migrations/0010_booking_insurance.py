# Generated by Django 5.0.4 on 2024-04-27 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0009_alter_booking_period_start_alter_busydate_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='insurance',
            field=models.CharField(default='normal or not', max_length=50),
            preserve_default=False,
        ),
    ]
