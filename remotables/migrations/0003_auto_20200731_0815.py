# Generated by Django 2.1.3 on 2020-07-31 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('remotables', '0002_auto_20191214_0848'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contentresource',
            old_name='unescaped_url',
            new_name='url',
        ),
        migrations.RenameField(
            model_name='ephemeralresource',
            old_name='unescaped_url',
            new_name='url',
        ),
    ]
