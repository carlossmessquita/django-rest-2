# Generated by Django 3.0.8 on 2021-11-25 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='rg',
            field=models.CharField(max_length=9, unique=True),
        ),
    ]
