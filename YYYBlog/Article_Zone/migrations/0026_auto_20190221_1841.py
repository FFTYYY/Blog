# Generated by Django 2.1.2 on 2019-02-21 10:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Article_Zone', '0025_auto_20190221_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='留言',
            name='创建时间',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 21, 10, 41, 41, 662930, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='节点',
            name='创建时间',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 21, 10, 41, 41, 661965, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='节点',
            name='最后修改时间',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 21, 10, 41, 41, 661965, tzinfo=utc)),
        ),
    ]