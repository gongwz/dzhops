# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HostList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.CharField(max_length=15, verbose_name='IP\u5730\u5740', blank=True)),
                ('hostname', models.CharField(max_length=30, verbose_name='\u4e3b\u673a\u540d')),
                ('minionid', models.CharField(max_length=60, verbose_name='MinionID')),
                ('nocn', models.CharField(max_length=30, verbose_name='\u8fd0\u8425\u5546\u5168\u79f0')),
                ('catagorycn', models.CharField(max_length=30, verbose_name='\u7c7b\u522b', blank=True)),
                ('pacn', models.CharField(max_length=30, verbose_name='\u5730\u533a\u5168\u79f0')),
                ('dccn', models.CharField(max_length=30, verbose_name='\u673a\u623f\u5168\u79f0', blank=True)),
                ('engineer', models.CharField(max_length=30, verbose_name='\u7ef4\u62a4\u4eba\u5458', blank=True)),
                ('remark', models.TextField(max_length=200, verbose_name='\u5907\u6ce8', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=50, verbose_name='\u7528\u6237\u540d', blank=True)),
                ('password', models.CharField(max_length=50, verbose_name='\u5bc6\u7801', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u7528\u6237\u7c7b\u578b', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='user_type',
            field=models.ForeignKey(to='app01.UserType'),
            preserve_default=True,
        ),
    ]
