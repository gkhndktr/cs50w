# Generated by Django 3.1.7 on 2021-06-13 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0024_auto_20210613_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Elektronik', 'Elektronik'), ('Mobilya', 'Mobilya'), ('Fashion', 'Fashion    '), ('Sports', 'Sports'), ('Hobbies', 'Hobbies'), ('No Category', 'No Category')], default='No category', max_length=64),
        ),
    ]
