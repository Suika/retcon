# Generated by Django 2.1.3 on 2019-12-31 23:49

from django.db import migrations, models
import django.db.models.deletion
import sharedstrings.models

def proxify_movies_and_tv():
    raise NotImplementedError

class Migration(migrations.Migration):

    dependencies = [
        ('sharedstrings', '0008_merge_20191124_1653'),
        ('retconpeople', '0020_person_uuid'),
        ('retconcreatives', '0023_auto_20191229_1306'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Franchise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=64)),
                ('name', sharedstrings.models.SharedStringField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='sharedstrings.Strings')),
            ],
        ),
        migrations.CreateModel(
            name='Portrayal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='retconpeople.Person')),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='retconcreatives.Episode')),
                ('role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='retconcreatives.Character')),
            ],
        ),
        # migrations.RemoveField(
        #     model_name='actor',
        #     name='acted_in',
        # ),
        # migrations.RemoveField(
        #     model_name='actor',
        #     name='person_ptr',
        # ),
        # migrations.RemoveField(
        #     model_name='movie',
        #     name='episode_ptr',
        # ),
        # migrations.RemoveField(
        #     model_name='tvepisode',
        #     name='movie_ptr',
        # ),
        migrations.DeleteModel(
            name='Actor',
        ),
        # migrations.RunPython(proxify_movies_and_tv),
        migrations.DeleteModel(
            name='Movie',
        ),
        migrations.DeleteModel(
            name='TVEpisode',
        ),
        migrations.AddField(
            model_name='character',
            name='franchise',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='retconcreatives.Franchise'),
        ),
        migrations.AddField(
            model_name='character',
            name='name',
            field=sharedstrings.models.SharedStringField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='sharedstrings.Strings'),
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('retconcreatives.episode',),
        ),
        migrations.CreateModel(
            name='TVEpisode',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('retconcreatives.episode',),
        ),
    ]
