# Generated by Django 2.1.3 on 2019-12-14 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContentResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unescaped_url', models.CharField(help_text='The url without any percent notation characters or plus substitutions of spaces', max_length=2000)),
                ('added_at', models.DateTimeField(auto_now=True)),
                ('valid_until', models.DateTimeField(null=True)),
                ('content_last_modified', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EphemeralResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unescaped_url', models.CharField(help_text='The url without any percent notation characters or plus substitutions of spaces', max_length=2000)),
                ('added_at', models.DateTimeField(auto_now=True)),
                ('valid_until', models.DateTimeField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
