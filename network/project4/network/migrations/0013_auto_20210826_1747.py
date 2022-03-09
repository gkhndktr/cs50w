# Generated by Django 3.2.5 on 2021-08-26 17:47

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0012_auto_20210826_1726'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='followed_by',
        ),
        migrations.RemoveField(
            model_name='user',
            name='follows',
        ),
        migrations.AddField(
            model_name='user',
            name='follower',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='follow_to', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='following',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='followed_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='creationTime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 8, 26, 17, 47, 33, 355220)),
        ),
    ]
