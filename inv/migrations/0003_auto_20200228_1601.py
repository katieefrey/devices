# Generated by Django 3.0.3 on 2020-02-28 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0002_proceedure'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='components',
            field=models.ManyToManyField(blank=True, null=True, to='inv.Component'),
        ),
    ]