# Generated by Django 5.0.4 on 2024-05-22 07:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0003_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 5, 22, 13, 14, 29, 347353)),
        ),
    ]
