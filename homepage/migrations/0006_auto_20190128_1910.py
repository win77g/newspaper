# Generated by Django 2.1.5 on 2019-01-28 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_auto_20190128_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='views',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=5),
        ),
    ]
