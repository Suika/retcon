# Generated by Django 2.1.3 on 2019-12-14 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remotables', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentresource',
            name='content_last_fetched',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contentresource',
            name='valid_until',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ephemeralresource',
            name='valid_until',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]