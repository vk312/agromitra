# Generated by Django 3.0.2 on 2020-01-23 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0004_auto_20200123_0941'),
    ]

    operations = [
        migrations.AddField(
            model_name='agriexpert',
            name='occupation',
            field=models.CharField(default='professor', max_length=25),
            preserve_default=False,
        ),
    ]
