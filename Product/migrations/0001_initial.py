# Generated by Django 5.0.4 on 2024-05-04 06:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categories', models.CharField(max_length=25)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='Product.categories')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=25)),
                ('price', models.IntegerField()),
                ('img', models.ImageField(upload_to='image')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.categories')),
            ],
        ),
    ]
