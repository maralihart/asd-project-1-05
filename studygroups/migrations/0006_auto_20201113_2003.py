# Generated by Django 3.1.1 on 2020-11-14 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studygroups', '0005_zoominfo_group_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studygroup',
            name='zoom',
        ),
        migrations.AddField(
            model_name='studygroup',
            name='group_id',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.DeleteModel(
            name='ZoomInfo',
        ),
    ]
