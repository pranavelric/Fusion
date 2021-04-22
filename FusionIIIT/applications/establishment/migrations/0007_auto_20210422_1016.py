# Generated by Django 3.1.5 on 2021-04-22 10:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('globals', '0003_auto_20191024_1242'),
        ('establishment', '0006_ltc_application_ltc_eligible_user_ltc_tracking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appraisal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discipline', models.CharField(max_length=30, null=True)),
                ('knowledge_field', models.CharField(max_length=30, null=True)),
                ('research_interest', models.CharField(max_length=60, null=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected'), ('forwarded', 'Forwarded'), ('auto rejected', 'Auto Rejected')], default='pending', max_length=20)),
                ('timestamp', models.DateTimeField(auto_now=True, null=True)),
                ('other_research_element', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('publications', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('conferences_meeting_attended', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('conferences_meeting_organized', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('admin_assign', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('sevice_to_ins', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('extra_info', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('faculty_comments', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_appraisals', to=settings.AUTH_USER_MODEL)),
                ('designation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='desig', to='globals.designation')),
            ],
        ),
        migrations.AlterField(
            model_name='cpda_application',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected'), ('forwarded', 'Forwarded'), ('auto rejected', 'Auto Rejected')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='ltc_application',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected'), ('forwarded', 'Forwarded'), ('auto rejected', 'Auto Rejected')], max_length=20, null=True),
        ),
        migrations.CreateModel(
            name='ThesisResearchSupervision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stud_name', models.CharField(max_length=30)),
                ('thesis_title', models.CharField(blank=True, max_length=30, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('semester', models.IntegerField()),
                ('status', models.CharField(max_length=30)),
                ('appraisal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicants_supervised_stud', to='establishment.appraisal')),
                ('co_supervisors', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_supervisors', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SponsoredProjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(max_length=30)),
                ('sponsoring_agency', models.CharField(max_length=30)),
                ('funding', models.IntegerField()),
                ('duration', models.IntegerField()),
                ('status', models.CharField(max_length=30)),
                ('remarks', models.CharField(max_length=30)),
                ('appraisal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicant_sponsored_projects', to='establishment.appraisal')),
                ('co_investigators', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_co_investigators', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NewCoursesOffered',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=30)),
                ('course_num', models.IntegerField(blank=True, null=True)),
                ('ug_or_pg', models.CharField(blank=True, max_length=2, null=True)),
                ('tutorial_hrs_wk', models.FloatField(blank=True, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('semester', models.IntegerField()),
                ('appraisal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicants_offered_new_courses', to='establishment.appraisal')),
            ],
        ),
        migrations.CreateModel(
            name='NewCourseMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=30)),
                ('course_num', models.IntegerField(blank=True, null=True)),
                ('ug_or_pg', models.CharField(blank=True, max_length=2, null=True)),
                ('activity_type', models.CharField(blank=True, max_length=10, null=True)),
                ('availiability', models.CharField(blank=True, max_length=10, null=True)),
                ('appraisal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicant_new_courses_material', to='establishment.appraisal')),
            ],
        ),
        migrations.CreateModel(
            name='CoursesInstructed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.IntegerField(blank=True, null=True)),
                ('course_name', models.CharField(max_length=30)),
                ('course_num', models.IntegerField(blank=True, null=True)),
                ('lecture_hrs_wk', models.FloatField(blank=True, null=True)),
                ('tutorial_hrs_wk', models.FloatField(blank=True, null=True)),
                ('lab_hrs_wk', models.FloatField(blank=True, null=True)),
                ('reg_students', models.IntegerField(blank=True, null=True)),
                ('appraisal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicant_courses', to='establishment.appraisal')),
                ('co_instructor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='co_inst', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AppraisalRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remark', models.CharField(blank=True, max_length=50, null=True)),
                ('permission', models.CharField(choices=[('intermediary', 'Intermediary Staff'), ('sanc_auth', 'Appraisal Sanctioning Authority'), ('sanc_off', 'Appraisal Sanctioning Officer')], default='sanc_auth', max_length=20)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected'), ('forwarded', 'Forwarded'), ('auto rejected', 'Auto Rejected')], default='pending', max_length=20)),
                ('appraisal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appraisal_requests', to='establishment.appraisal')),
                ('requested_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_appraisal_requests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AppraisalAdministrators',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authority', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sanc_authority_of_ap', to='globals.designation')),
                ('officer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sanc_officer_of_ap', to='globals.designation')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='apprasial_admins', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
