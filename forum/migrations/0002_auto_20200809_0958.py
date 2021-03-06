# Generated by Django 3.0.7 on 2020-08-09 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='prijava',
            field=models.IntegerField(choices=[(0, 'Prijavi'), (1, 'Ne želim')], default=1),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(0, 'Objavljeno'), (1, 'Nije objavljeno')], default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='tekst',
            field=models.CharField(default='Napiši svoju priču!', max_length=1000),
        ),
    ]
