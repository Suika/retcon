# Generated by Django 2.2.14 on 2020-08-28 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remotables', '0003_auto_20200731_0815'),
        ('retconpeople', '0028_auto_20200731_0815'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='external_representation',
            new_name='external_representations'
        ),
    ]
