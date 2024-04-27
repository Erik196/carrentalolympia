# Generated by Django 5.0.4 on 2024-04-21 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0006_unavailabledate'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusyDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_id', models.IntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='booking',
            name='period_end',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='period_start',
            field=models.DateField(),
        ),
    ]