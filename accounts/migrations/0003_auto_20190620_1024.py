# Generated by Django 2.2.2 on 2019-06-20 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190620_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userquota',
            name='current_usage_mb',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='userquota',
            name='max_usage_mb',
            field=models.FloatField(default=1000),
        ),
    ]
