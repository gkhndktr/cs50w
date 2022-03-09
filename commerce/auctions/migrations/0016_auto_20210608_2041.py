# Generated by Django 3.1.7 on 2021-06-08 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0015_auto_20210531_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='comments',
            field=models.ManyToManyField(blank=True, null=True, related_name='comments', to='auctions.comment'),
        ),
        migrations.AddField(
            model_name='product',
            name='winner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='winners', to='auctions.bid'),
        ),
    ]
