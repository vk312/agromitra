# Generated by Django 3.0.2 on 2020-01-23 10:19

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0006_agriexpert_field_of_interest'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgriAssistance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assistant_name', models.CharField(max_length=50)),
                ('phone', phone_field.models.PhoneField(blank=True, max_length=31)),
                ('aadhar_no', models.BigIntegerField()),
                ('mpin', models.IntegerField()),
                ('taluka', models.CharField(max_length=25)),
                ('city', models.CharField(max_length=25)),
                ('state', models.CharField(max_length=25)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
    ]
