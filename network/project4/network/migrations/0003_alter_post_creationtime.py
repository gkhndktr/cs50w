# Generated by Django 3.2.5 on 2021-08-07 08:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_alter_post_creationtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='creationTime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 8, 7, 8, 26, 36, 224061)),
        ),
    ]
