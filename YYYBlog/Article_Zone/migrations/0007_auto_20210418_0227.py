# Generated by Django 3.1.2 on 2021-04-17 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Article_Zone', '0006_附加_类型'),
    ]

    operations = [
        migrations.AlterField(
            model_name='节点',
            name='附加内容',
            field=models.ManyToManyField(blank=True, related_name='所在', to='Article_Zone.附加'),
        ),
    ]
