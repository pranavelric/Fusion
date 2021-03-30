# Generated by Django 3.1.5 on 2021-03-30 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academic_information', '0005_auto_20200522_1851'),
        ('academic_procedures', '0018_merge_20210330_1358'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseRequested',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curr_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.curriculum')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.student')),
            ],
            options={
                'db_table': 'AddCourses',
            },
        ),
    ]
