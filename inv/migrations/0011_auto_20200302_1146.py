# Generated by Django 3.0.3 on 2020-03-02 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0010_auto_20200302_1128'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proceedure',
            old_name='checking',
            new_name='checking_notes',
        ),
        migrations.RenameField(
            model_name='proceedure',
            old_name='cleaning',
            new_name='cleaning_notes',
        ),
        migrations.RenameField(
            model_name='proceedure',
            old_name='location',
            new_name='location_notes',
        ),
    ]
