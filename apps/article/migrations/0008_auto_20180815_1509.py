# Generated by Django 2.0.6 on 2018-08-15 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_auto_20180815_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='add_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='发表时间'),
        ),
        migrations.AlterField(
            model_name='commentreplay',
            name='add_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='发表时间'),
        ),
    ]
