# Generated by Django 2.1.3 on 2020-01-05 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retconstorage', '0001_initial'),
        ('remotables', '0002_auto_20191214_0848'),
        ('retconcreatives', '0024_auto_20191231_2349'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='external_representation',
            field=models.ManyToManyField(blank=True, related_name='_company_external_representation_+', to='remotables.ContentResource'),
        ),
        migrations.AddField(
            model_name='creativework',
            name='files',
            field=models.ManyToManyField(blank=True, related_name='_creativework_files_+', to='retconstorage.ManagedFile'),
        ),
    ]
