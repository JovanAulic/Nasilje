# Generated by Django 3.0.7 on 2020-08-09 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0008_auto_20200809_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tuzba',
            field=models.IntegerField(choices=[(0, 'Neću'), (1, 'Hoću')], default=0),
        ),
    ]
