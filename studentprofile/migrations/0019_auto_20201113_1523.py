# Generated by Django 3.1.1 on 2020-11-13 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentprofile', '0018_student_groupme_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
