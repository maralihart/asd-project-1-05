# Generated by Django 3.1 on 2020-11-10 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentprofile', '0016_auto_20201110_1619'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='phoneNumber',
            new_name='phone',
        ),
    ]
