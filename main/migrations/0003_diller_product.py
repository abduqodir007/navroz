# Generated by Django 5.0.8 on 2024-08-19 12:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_number_person_age_person_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50)),
                ('foto', models.ImageField(upload_to='media')),
                ('ball', models.IntegerField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=250)),
                ('product_weight', models.FloatField()),
                ('product_price', models.FloatField()),
                ('product_quantity', models.FloatField()),
                ('diller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diller_product', to='main.diller')),
            ],
        ),
    ]
