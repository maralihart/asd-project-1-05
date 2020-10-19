# Generated by Django 3.1.1 on 2020-10-19 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentprofile', '0010_student_num'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudyGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('maxSize', models.PositiveSmallIntegerField(default=2)),
                ('members', models.ManyToManyField(to='studentprofile.Student')),
            ],
        ),
    ]
