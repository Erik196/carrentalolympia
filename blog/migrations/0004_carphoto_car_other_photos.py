# Generated by Django 5.0.2 on 2024-04-07 14:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_car_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='cars/others/')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.car')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='other_photos',
            field=models.ManyToManyField(blank=True, related_name='cars', to='blog.carphoto'),
        ),
    ]
