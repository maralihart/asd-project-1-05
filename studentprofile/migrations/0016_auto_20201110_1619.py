# Generated by Django 3.1 on 2020-11-10 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentprofile', '0015_auto_20201110_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phoneNumber',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]