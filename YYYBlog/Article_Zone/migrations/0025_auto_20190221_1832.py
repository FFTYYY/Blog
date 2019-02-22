# Generated by Django 2.1.2 on 2019-02-21 10:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Article_Zone', '0024_留言_对象'),
    ]

    operations = [
        migrations.AddField(
            model_name='留言',
            name='创建时间',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 21, 10, 32, 38, 13217, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='节点',
            name='创建时间',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 21, 10, 32, 38, 12219, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='节点',
            name='最后修改时间',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
