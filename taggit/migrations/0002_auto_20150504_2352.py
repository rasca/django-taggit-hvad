# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('language_code', models.CharField(max_length=15, db_index=True)),
                ('master', models.ForeignKey(related_name='translations', editable=False, to='taggit.Tag', null=True)),
            ],
            options={
                'managed': True,
                'abstract': False,
                'db_table': 'taggit_tag_translation',
                'db_tablespace': '',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='tagtranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.RemoveField(
            model_name='tag',
            name='name',
        ),
    ]
