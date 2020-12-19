# Generated by Django 3.1.4 on 2020-12-19 07:40

import apps.room.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='code',
            field=models.CharField(default=apps.room.models.generate_unique_code, max_length=8, unique=True),
        ),
    ]
