# Generated by Django 3.1.6 on 2021-02-18 14:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trees', '0002_auto_20210218_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tree',
            name='circuit',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(500)]),
        ),
    ]
