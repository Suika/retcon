# Generated by Django 2.1.3 on 2019-09-20 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('retconpeople', '0007_auto_20190920_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='parent_site',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='child_sites', to='retconpeople.Website'),
        ),
        migrations.AlterField(
            model_name='website',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='_website_tags_+', to='semantictags.Tag'),
        ),
        migrations.AlterField(
            model_name='website',
            name='user_number_pattern',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='website',
            name='username_pattern',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]