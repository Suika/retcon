# Generated by Django 2.1.3 on 2019-11-24 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('retconpeople', '0014_merge_20191124_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='username',
            name='belongs_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usernames', to='retconpeople.Person'),
        ),
        migrations.AlterField(
            model_name='username',
            name='website',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_names', to='retconpeople.Website'),
        ),
    ]
