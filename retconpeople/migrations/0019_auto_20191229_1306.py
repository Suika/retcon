# Generated by Django 2.1.3 on 2019-12-29 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retconpeople', '0018_auto_20191228_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='description',
            field=models.CharField(blank=True, max_length=512),
        ),
    ]
