# Generated by Django 5.0.4 on 2024-05-27 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0013_booking_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='insurance',
            field=models.CharField(choices=[('easy', 'Easy'), ('complicate', 'Complicate')], max_length=10),
        ),
    ]