# Generated by Django 2.2.2 on 2019-07-18 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0021_auto_20190718_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='folder',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
