# Generated by Django 3.0.7 on 2020-08-09 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_auto_20200809_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='prijava',
            field=models.IntegerField(choices=[(0, 'Prijavi'), (1, 'Ne želim')], default=1),
        ),
    ]