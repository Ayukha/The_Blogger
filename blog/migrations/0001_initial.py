# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organiser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=63)),
                ('slug', models.SlugField(help_text='A label for URL config', unique_for_month='pub_date', max_length=63)),
                ('text', models.TextField()),
                ('pub_date', models.DateField(verbose_name='date published', auto_now_add=True)),
                ('startups', models.ManyToManyField(related_name='blog_posts', to='organiser.Startup')),
                ('tags', models.ManyToManyField(related_name='blog_posts', to='organiser.Tag')),
            ],
            options={
                'verbose_name': 'blog post',
                'ordering': ['-pub_date', 'title'],
                'get_latest_by': 'pub_date',
            },
        ),
    ]
