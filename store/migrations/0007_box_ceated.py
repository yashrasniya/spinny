# Generated by Django 4.2.4 on 2023-08-25 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_box_area_box_volume'),
    ]

    operations = [
        migrations.AddField(
            model_name='box',
            name='Ceated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
