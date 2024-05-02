# Generated by Django 5.0.4 on 2024-04-16 21:53

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_delete_booking'),
        ('bookings', '0003_alter_booking_car_delete_cars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.car'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='period_end',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.CreateModel(
            name='UnavailableDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.car')),
            ],
        ),
    ]
