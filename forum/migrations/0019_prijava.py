# Generated by Django 3.0.7 on 2020-08-24 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0018_auto_20200819_1051'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prijava',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime', models.CharField(default='Unesite Vaše ime', max_length=30)),
                ('prezime', models.CharField(default='Unesite Vaše prezime', max_length=50)),
                ('jedinstveni_maticni_broj', models.IntegerField(max_length=13)),
                ('vrsta_nasilja', models.CharField(default='Izaberite vrstu nasilju', max_length=20)),
                ('objekat', models.CharField(default='Da li ste vi žrtva nasilja?', max_length=20)),
                ('pol', models.CharField(default='Izaberite pol', max_length=20)),
                ('lokacija', models.CharField(default='Unesite Vašu adresu?', max_length=200)),
                ('starost', models.IntegerField(max_length=10)),
            ],
        ),
    ]
