# Generated by Django 2.1.1 on 2019-10-25 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sharedstrings', '0005_auto_20190922_1607'),
        ('retconpeople', '0011_auto_20191007_2356'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='ambiguous_tags',
            field=models.ManyToManyField(blank=True, to='sharedstrings.Strings'),
        ),
        migrations.AlterField(
            model_name='website',
            name='domain',
            field=models.CharField(help_text='e.g. twitter.com', max_length=256),
        ),
        migrations.AlterField(
            model_name='website',
            name='user_number_pattern',
            field=models.CharField(blank=True, help_text='regex with capture group for string after url scheme e.g.\n pixiv\\.net/member\\.php\\?id=\\d+', max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='website',
            name='username_pattern',
            field=models.CharField(blank=True, help_text='regex with capture group for string after url scheme e.g.\n twitter\\.com/([^/]+)', max_length=1024, null=True),
        ),
    ]
