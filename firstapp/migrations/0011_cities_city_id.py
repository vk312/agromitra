# Generated by Django 3.0.2 on 2020-02-02 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0010_cities'),
    ]

    operations = [
        migrations.AddField(
            model_name='cities',
            name='city_id',
            field=models.IntegerField(auto_created=True, default=1),
            preserve_default=False,
        ),
    ]