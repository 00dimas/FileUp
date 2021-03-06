# Generated by Django 2.2.2 on 2019-06-15 09:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0003_file_file_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='folder',
            name='date_recycled',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='folder',
            name='is_recycled',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='folder',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
