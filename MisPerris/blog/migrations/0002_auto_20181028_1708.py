# Generated by Django 2.1.2 on 2018-10-28 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postulantes',
            options={'permissions': (('postulante', 'Postulante'),)},
        ),
    ]
