# Generated by Django 3.1.1 on 2020-09-14 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurements', '0002_auto_20200914_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='apellido',
            field=models.CharField(max_length=30, verbose_name='apellido de la persona'),
        ),
    ]
