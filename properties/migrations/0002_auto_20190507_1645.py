# Generated by Django 2.2.1 on 2019-05-07 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='propertyimage',
            old_name='Property_id',
            new_name='Property',
        ),
    ]