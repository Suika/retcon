# Generated by Django 2.1.3 on 2019-09-20 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retconcreatives', '0011_auto_20190920_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creativework',
            name='published_on',
            field=models.DateField(null=True),
        ),
    ]
